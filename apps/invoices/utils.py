from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_invoice_pdf(invoice):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    p.setFont("Helvetica-Bold", 20)
    p.drawString(200, 800, "Invoice")

    # Customer Info
    p.setFont("Helvetica", 12)
    p.drawString(50, 770, f"Invoice Number: {invoice.invoice_number}")
    p.drawString(50, 750, f"Customer: {invoice.customer.name}")
    p.drawString(50, 735, f"Email: {invoice.customer.email}")
    p.drawString(50, 720, f"Address: {invoice.customer.address}")
    p.drawString(50, 700, f"Date: {invoice.date}")

    # Table headers
    p.drawString(50, 660, "Product")
    p.drawString(250, 660, "Quantity")
    p.drawString(350, 660, "Price")
    p.drawString(450, 660, "Total")

    y = 640
    total_amount = 0

    for item in invoice.items.all():
        line_total = item.quantity * item.price
        total_amount += line_total

        p.drawString(50, y, item.product.name)
        p.drawString(250, y, str(item.quantity))
        p.drawString(350, y, f"{item.price:.2f}")
        p.drawString(450, y, f"{line_total:.2f}")
        y -= 20

    # Grand total
    p.setFont("Helvetica-Bold", 12)
    p.drawString(350, y - 20, "Total:")
    p.drawString(450, y - 20, f"{total_amount:.2f}")

    p.showPage()
    p.save()
    buffer.seek(0)

    return buffer
