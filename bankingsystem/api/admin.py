from django.contrib import admin
from api.models import Customer, Loan, Transaction


admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Transaction)