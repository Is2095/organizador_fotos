from datetime import datetime
from pathlib import Path
import shutil

def generar_nombre(fecha: datetime, extension: str):
  """Genera el nombre de una fotografía a partir de su fecha."""

  fecha_formateada = fecha.strftime("%Y-%m-%d_%H-%M-%S")

  return f"{fecha_formateada}{extension.lower()}"

def generar_nombre_disponible(
    fecha: datetime,
    extension: str,
    carpeta_salida: Path
):
  """Genera un nombre que no exista en la carpeta de salida."""

  nombre_base = generar_nombre(fecha, extension)

  ruta_destino = carpeta_salida / nombre_base

  if not ruta_destino.exists():
    return nombre_base

  contador = 1

  while True:
    nombre_nuevo = (
      f"{fecha.strftime('%Y-%m-%d_%H-%M-%S')}"
      f"_{contador:02d}"
      f"{extension.lower()}"
    )

    ruta_destino = carpeta_salida / nombre_nuevo

    if not ruta_destino.exists():
      return nombre_nuevo

    contador += 1

def copiar_fotografia(
    ruta_origen: Path,
    carpeta_salida: Path,
    nombre_nuevo: str
):
  """Copia una fotografía a la carpeta de salida."""

  ruta_destino = carpeta_salida / nombre_nuevo

  shutil.copy2(ruta_origen, ruta_destino)

  return ruta_destino