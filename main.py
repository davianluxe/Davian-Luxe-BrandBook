# =====================================
# MAIN - DAVIAN LUXE BRAND BOOK
# =====================================

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from utils import crear_carpetas
from sections.portada import crear_portada
from sections.historia import crear_historia
from sections.mision import crear_mision
from utils import crear_carpetas

# Crear carpetas automáticamente
crear_carpetas()

# Crear PDF
pdf = canvas.Canvas(
    "output/Davian_Luxe_BrandBook.pdf",
    pagesize=A4
)

ANCHO, ALTO = A4

# ============================
# PORTADA
# ============================

crear_portada(pdf)

crear_historia(pdf)

crear_mision(pdf)

pdf.save()

print("===================================")
print("DAVIAN LUXE BRAND BOOK")
print("PDF creado correctamente")
print("===================================")
