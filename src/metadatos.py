from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def leer_exif(ruta_foto: Path):
    """Lee todos los metadatos EXIF de una fotografía."""

    with Image.open(ruta_foto) as imagen:
        exif = imagen.getexif()

        metadatos = {}

        for etiqueta, valor in exif.items():
            nombre = TAGS.get(etiqueta, etiqueta)

            if nombre == "GPSInfo":
                gps = exif.get_ifd(0x8825)

                if gps:
                    valor = leer_gps(gps)

            metadatos[nombre] = valor

        return metadatos


def leer_gps(gps_info):
    """Convierte las etiquetas GPS a nombres legibles."""

    gps = {}

    for etiqueta, valor in gps_info.items():
        nombre = GPSTAGS.get(etiqueta, etiqueta)
        gps[nombre] = valor

    return gps


def obtener_fechas_exif(ruta_foto: Path):
    """Obtiene las diferentes fechas disponibles en los metadatos EXIF."""

    with Image.open(ruta_foto) as imagen:
        exif = imagen.getexif()

        fechas = {
            "DateTimeOriginal": None,
            "DateTimeDigitized": None,
            "DateTime": None,
        }

        for etiqueta, valor in exif.items():
            nombre = TAGS.get(etiqueta, etiqueta)

            if nombre in fechas:
                fechas[nombre] = valor

        return fechas