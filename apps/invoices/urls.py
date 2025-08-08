from django.urls import path
from .views import invoice_pdf_view

urlpatterns = [
    path('invoice/<int:pk>/pdf/', invoice_pdf_view, name='invoice-pdf'),
]
