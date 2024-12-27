from django.contrib import admin
from .models import Seller, CreditRequest


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit')
    search_fields = ('name',)
    list_filter = ('credit',)


@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'amount', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('seller__name',)
    actions = ['approve_requests']

    def approve_requests(self, request, queryset):
        for credit_request in queryset:
            if not credit_request.approved:
                credit_request.approve()
        self.message_user(request, "Selected requests have been approved.")
    approve_requests.short_description = "Approve selected credit requests"