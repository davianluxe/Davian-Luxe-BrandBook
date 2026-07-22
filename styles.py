from config import *

def titulo(pdf, texto, y):
    pdf.setFillColor(COLOR_AZUL)
    pdf.setFont(FUENTE_TITULO, 28)
    pdf.drawString(MARGEN, y, texto)

def subtitulo(pdf, texto, y):
    pdf.setFillColor(COLOR_DORADO)
    pdf.setFont(FUENTE_TEXTO, 18)
    pdf.drawString(MARGEN, y, texto)

def parrafo(pdf, texto, y):
    pdf.setFillColor(COLOR_GRIS)
    pdf.setFont(FUENTE_TEXTO, 12)
    pdf.drawString(MARGEN, y, texto)
