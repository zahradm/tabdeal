from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'transaction_type', 'amount', 'timestamp')
    search_fields = ('seller__name',)
    list_filter = ('transaction_type', 'timestamp')
