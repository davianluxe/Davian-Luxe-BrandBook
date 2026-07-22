from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

pdf = canvas.Canvas("Davian_Luxe_BrandBook.pdf", pagesize=A4)

ancho, alto = A4

# Fondo blanco
pdf.setFillColor(HexColor("#FFFFFF"))
pdf.rect(0, 0, ancho, alto, fill=1)

# Título
pdf.setFillColor(HexColor("#0B3D91"))
pdf.setFont("Helvetica-Bold", 30)
pdf.drawCentredString(ancho/2, 750, "DAVIAN LUXE")

# Subtítulo
pdf.setFillColor(HexColor("#C9A227"))
pdf.setFont("Helvetica", 18)
pdf.drawCentredString(ancho/2, 715, "Brand Book")

# Eslogan
pdf.setFillColor(HexColor("#444444"))
pdf.setFont("Helvetica", 12)
pdf.drawCentredString(ancho/2, 60, "Premium Living • Exclusive Life")

pdf.save()

print("Brand Book creado correctamente.")
