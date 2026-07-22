from styles import titulo, parrafo

def crear_historia(pdf):

    # Crear una nueva página
    pdf.showPage()

    # Título
    titulo(pdf, "Nuestra Historia", 760)

    # Texto
    texto = (
        "Davian Luxe nace con la visión de transformar la forma en que las personas "
        "viven su hogar. Nuestra marca reúne productos premium para la cocina, el "
        "bienestar, la salud y el desarrollo empresarial, ofreciendo calidad, "
        "innovación y una experiencia exclusiva en cada detalle."
    )

    # Dibujar el texto en varias líneas
    y = 720

    for linea in [
        "Davian Luxe nace con la visión de transformar la forma",
        "en que las personas viven su hogar.",
        "",
        "Nuestra marca reúne productos premium para la cocina,",
        "el bienestar, la salud y el desarrollo empresarial.",
        "",
        "Cada producto es seleccionado bajo criterios de",
        "calidad, innovación, elegancia y exclusividad.",
    ]:
        parrafo(pdf, linea, y)
        y -= 20
