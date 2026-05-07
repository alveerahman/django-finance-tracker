from django.shortcuts import render
from .models import Transaction
from django.db.models import Sum


def dashboard(request):
    data = Transaction.objects.all().order_by('-date')
    total_in = data.filter(transaction_type='Income').aggregate(
        Sum('amount'))['amount__sum'] or 0
    total_ex = data.filter(transaction_type='Expense').aggregate(
        Sum('amount'))['amount__sum'] or 0
    return render(request, 'dashboard.html', {
        'transactions': data,
        'balance': total_in - total_ex,
        'income': total_in,
        'expense': total_ex
    })
