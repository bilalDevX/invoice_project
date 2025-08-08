from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Invoice
from .utils import generate_invoice_pdf

def invoice_pdf_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    pdf_buffer = generate_invoice_pdf(invoice)
    return FileResponse(pdf_buffer, as_attachment=True, filename=f"invoice_{invoice.invoice_number}.pdf")
