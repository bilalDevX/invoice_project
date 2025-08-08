from django.contrib import admin
from .models import Customer, Product, Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('invoice_number', 'customer', 'date')

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Invoice, InvoiceAdmin)
