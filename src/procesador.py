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

def procesar_fotografia(ruta_foto: Path):
    """Lee y procesa los metadatos de una fotografía."""

    metadatos = leer_exif(ruta_foto)

    if not metadatos:
        return {
            "ruta": ruta_foto,
            "metadatos":{},
            "fechas": {},
            "fecha": None,
            "tiene_exif": False,
            "estado": "SIN_EXIF"
        }

    fechas = obtener_fechas_exif(metadatos)
    fecha = obtener_fecha_foto(metadatos)

    if fecha is None:
        estado = "SIN_FECHA"
    else:
        estado = "CON_FECHA"

    return {
        "ruta": ruta_foto,
        "metadatos": metadatos,
        "fechas": fechas,
        "fecha": fecha,
        "tiene_exif": True,
        "estado": estado,
    }
