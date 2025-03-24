from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    balance_amount = models.FloatField(default=10000)

    def __str__(self):
        return self.name

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    interest_rate = models.IntegerField(default=6)
    loan_period = models.IntegerField()
    total_amount = models.FloatField(default=0)
    monthly_emi = models.FloatField(default=0)
    no_of_emis = models.IntegerField(default=0)
    remaining_amount = models.FloatField(default=0)
    loan_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name

    def save(self, *args, **kwargs):
        self.total_amount = self.remaining_amount = self.loan_amount + (self.loan_amount * self.interest_rate / 100)
        self.monthly_emi = self.total_amount / self.loan_period
        self.no_of_emis = self.loan_period
        super(Loan, self).save(*args, **kwargs)

    def special_save(self, *args, **kwargs):
        super(Loan, self).save(*args, **kwargs)
    #another save method so that i can save the loan and not update the same thing over and over again and wonder why is it not updating the amound and emi =(.

class Transaction(models.Model):
    TYPE = [
        ('LEND', 'LEND'),
        ('LUMPSUM', 'LUMPSUM'),
        ('EMI', 'EMI'),
    ]
    #NOTE : transaction_type should be credit or debit but since you asked for a banking system to lend money to borrowers and receive payment for the loans i have added these.
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #I don't think there is any need for customer in transaction in this type of banking system but still added it.
    # had to add customer in form-data while posting, so commented it out.
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    transaction_amount = models.FloatField()
    transaction_type = models.CharField(max_length=10, choices=TYPE, default='EMI')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)