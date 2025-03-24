from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from api.models import Customer, Loan, Transaction
from api.serializers import LoanSerializer, TransactionSerializer

class APIViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], name='lend')
    def lend(self, request):
        data = request.data
        loanser = LoanSerializer(data=data)
        if loanser.is_valid():
            loan = loanser.save()
            transaction = Transaction.objects.create(loan=loan, transaction_amount=loan.loan_amount, transaction_type='LEND')
            customer = get_object_or_404(Customer, pk=loan.customer.id)
            customer.balance_amount += loan.loan_amount
            customer.save()
            return Response({
                'loan_id': loan.id,
                'total_amount': "{:.2f}".format(loan.total_amount),
                'monthly_emi': "{:.2f}".format(loan.monthly_emi),
                'no_of_emis': loan.no_of_emis,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(loanser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'], name='payment')
    def payment(self, request):
        data = request.data
        transaction_ser = TransactionSerializer(data=data)
        if transaction_ser.is_valid():
            transaction = transaction_ser.save()
            if transaction.transaction_type == 'LUMPSUM':
                loan = get_object_or_404(Loan, pk=transaction.loan.id)
                loan.remaining_amount -= transaction.transaction_amount
                loan.monthly_emi = loan.remaining_amount/loan.no_of_emis
                customer = get_object_or_404(Customer, pk=loan.customer.id)
                customer.balance_amount -= transaction.transaction_amount
                customer.save()
                loan.special_save()
            else:
                loan = get_object_or_404(Loan, pk=transaction.loan.id)
                loan.remaining_amount -= transaction.transaction_amount
                loan.no_of_emis -= 1
                customer = get_object_or_404(Customer, pk=loan.customer.id)
                customer.balance_amount -= transaction.transaction_amount
                customer.save()
                loan.special_save()

            return Response({
                'total_amount': "{:.2f}".format(loan.total_amount),
                'remaining_amount': "{:.2f}".format(loan.remaining_amount),
                'monthly_emi': "{:.2f}".format(loan.monthly_emi),
                'no_of_emis': loan.no_of_emis
            }, status=status.HTTP_200_OK)
        else:
            return Response(transaction_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name='ledger')
    def ledger(self, request):
        try:
            data = request.data
            loan = get_object_or_404(Loan, pk=data['loan'])
            customer = get_object_or_404(Customer, pk=loan.customer.id)
            Transactions = Transaction.objects.filter(loan=loan)
            transaction_ser = TransactionSerializer(Transactions, many=True)
            data = {
                'balance_amount' : customer.balance_amount,
                'total_amount': loan.total_amount,
                'remaining_amount': loan.remaining_amount,
                'monthly_emi': loan.monthly_emi,
                'no_of_emis': loan.no_of_emis
            }
            data['transactions'] = transaction_ser.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], name='account_overview')
    def account_overview(self,request):
        try:
            customer = get_object_or_404(Customer, pk=request.data['customer'])
            loan = Loan.objects.filter(customer=customer)
            loan_ser = LoanSerializer(loan, many=True)
            data = {
                'name': customer.name,
                'balance_amount' : customer.balance_amount,
            }
            data['loans'] = loan_ser.data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

