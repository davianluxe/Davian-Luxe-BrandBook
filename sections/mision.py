from styles import titulo, parrafo

def crear_mision(pdf):

    pdf.showPage()

    titulo(pdf, "Nuestra Misión", 760)

    lineas = [
        "Inspirar y transformar la vida de las personas mediante",
        "productos premium para el hogar, la salud, la cocina",
        "inteligente y el bienestar.",
        "",
        "En Davian Luxe buscamos ofrecer experiencias de",
        "excelencia, confianza e innovación, generando valor",
        "para nuestros clientes y oportunidades de crecimiento",
        "para nuestros aliados comerciales."
    ]

    y = 720

    for linea in lineas:
        parrafo(pdf, linea, y)
        y -= 20
