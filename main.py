from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Davian_Luxe.pdf")

pdf.setFont("Helvetica-Bold", 24)

pdf.drawString(100, 750, "DAVIAN LUXE")

pdf.setFont("Helvetica", 16)

pdf.drawString(100, 720, "Hola Luis, este es nuestro primer PDF.")

pdf.save()

print("PDF creado correctamente.")
