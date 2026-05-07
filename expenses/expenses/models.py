from django.db import models


class Transaction(models.Model):
    TYPES = (('Income', 'Income'), ('Expense', 'Expense'))
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TYPES)
    date = models.DateField(auto_now_add=True)
