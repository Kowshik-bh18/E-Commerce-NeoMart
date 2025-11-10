from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from io import BytesIO

def generate_invoice_pdf(order):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Header
    p.setFont("Helvetica-Bold", 24)
    p.drawString(50, height - 50, "Invoice")
    
    # Order info
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Order #{order.id}")
    p.drawString(50, height - 100, f"Date: {order.created_at.strftime('%Y-%m-%d')}")
    p.drawString(50, height - 120, f"Customer: {order.user.username}")
    
    # Items table
    data = [["Product", "Quantity", "Price", "Total"]]
    for item in order.items.all():
        data.append([
            item.product.name,
            str(item.quantity),
            f"${item.price:.2f}",
            f"${(item.quantity * item.price):.2f}"
        ])
    
    table = Table(data, colWidths=[200, 100, 100, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    table.wrapOn(p, width, height)
    table.drawOn(p, 50, height - 300)
    
    # Total
    p.setFont("Helvetica-Bold", 14)
    p.drawString(350, height - 350, f"Total Amount: ${order.total_amount:.2f}")
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer