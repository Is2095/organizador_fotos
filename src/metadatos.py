from pathlib import Path
from datetime import datetime

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


def obtener_fechas_exif(metadatos):
    """Obtiene las diferentes fechas disponibles en los metadatos EXIF."""

    fechas = {
      "DateTimeOriginal": None,
      "DateTimeDigitized": None,
      "DateTime": None,
    }
    for etiqueta, valor in metadatos.items():
      nombre = TAGS.get(etiqueta, etiqueta)

      if nombre in fechas:
        fechas[nombre] = valor

    return fechas

def obtener_fecha_foto(metadatos):
  """Obtiene la mejor fecha disponible de la totografía."""

  fechas = obtener_fechas_exif(metadatos)

  prioridad = [
      "DateTimeOriginal",
      "DateTimeDigitized",
      "DateTime"
  ]

  for nombre in prioridad:
    valor = fechas[nombre]
    if valor is None:
      continue
    try:
      return datetime.strptime(valor, "%Y:%m:%d %H:%M:%S")
    except ValueError:
      continue

    