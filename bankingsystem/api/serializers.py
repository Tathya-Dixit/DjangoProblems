from rest_framework import serializers
from api.models import Customer, Loan, Transaction

class LoanSerializer(serializers.ModelSerializer):
    amount_paid = serializers.SerializerMethodField()
    class Meta:
        model = Loan
        fields = '__all__'
    
    def get_amount_paid(self, obj):
        return obj.loan_amount - obj.remaining_amount

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
