from pathlib import Path

from metadatos import (
    leer_exif,
    obtener_fechas_exif,
    obtener_fecha_foto
)


def obtener_fotografias(carpeta_entrada: Path):
    
    """Obtiene las fotografías disponibles en la carpeta de entrada."""

    extensiones_validas = {
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".tif",
        ".tiff",
    }

    fotografias = []

    for archivo in carpeta_entrada.iterdir():

        if not archivo.is_file():
            continue

        if archivo.suffix.lower() not in extensiones_validas:
            continue

        fotografias.append(archivo)

    return fotografias

def procesar_fotografias(ruta_foto: Path):
    """Lee y procesa los metadatos de una fotografía."""

    metadatos = leer_exif(ruta_foto)

    if not metadatos:
        return None

    fechas = obtener_fechas_exif(metadatos)
    fecha = obtener_fecha_foto(metadatos)

    return {
        "ruta": ruta_foto,
        "metadatos": metadatos,
        "fechas": fechas,
        "fecha": fecha

    }
