from pathlib import Path

def crear_carpetas():
    carpetas = [
        "assets",
        "sections",
        "output"
    ]

    for carpeta in carpetas:
        Path(carpeta).mkdir(exist_ok=True)
