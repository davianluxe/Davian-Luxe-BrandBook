from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# =====================================
# CREAR ESTRUCTURA DEL PROYECTO
# =====================================

carpetas = [
    "assets",
    "sections",
    "output"
]

for carpeta in carpetas:
    Path(carpeta).mkdir(exist_ok=True)

print("✅ Carpetas creadas correctamente.")

# =====================================
# CREAR PDF
# =====================================

pdf = canvas.Canvas(
    "output/Davian_Luxe_BrandBook.pdf",
    pagesize=A4
)

pdf.setFont("Helvetica-Bold", 28)
pdf.drawString(100, 780, "DAVIAN LUXE")

pdf.setFont("Helvetica", 18)
pdf.drawString(100, 745, "Brand Book")

pdf.save()

print("✅ PDF creado correctamente.")
