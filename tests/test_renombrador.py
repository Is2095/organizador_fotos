from datetime import datetime
from pathlib import Path

from src.renombrador import (
  generar_nombre,
  generar_nombre_disponible,
  copiar_fotografia
)

from src.metadatos import obtener_fecha_foto

def test_generar_nombre():
  fecha = datetime(2026, 8, 1, 15, 42, 18)

  resultado = generar_nombre(fecha, ".jpg")

  assert resultado == "2026-08-01_15-42-18.jpg"

def test_generar_nombre_disponible(tmp_path: Path):
    fecha = datetime(2026, 8, 1, 15, 42, 18)

    nombre_original = "2026-08-01_15-42-18.jpg"

    (tmp_path / nombre_original).touch()

    resultado = generar_nombre_disponible(
        fecha,
        ".jpg",
        tmp_path
    )

    assert resultado == "2026-08-01_15-42-18_01.jpg"

def test_obtener_fecha_foto_usa_datetime():
  metadatos = {
      
    "DateTime": "2026:08:01 15:42:18"      
  }

  resultado = obtener_fecha_foto(metadatos)

  assert resultado == datetime(2026, 8, 1, 15, 42, 18)

def test_obtener_fecha_foto_prioriza_datetime_original():
  metadatos = {
    "DateTimeOriginal": "2026:01:16 22:52:41",
    "DateTimeDigitized": "2026:01:16 22:52:42",
    "DateTime": "2026:01:16 22:52:43"
  }

  resultado = obtener_fecha_foto(metadatos)

  assert resultado == datetime(2026, 1, 16, 22, 52, 41)

def test_obtener_fecha_foto_usa_datetime_digitized():
  metadatos = {
    "DateTimeDigitized": "2026:04:19 21:56:33",
    "DateTime": "2026:04:19 21:56:34"
  }

  resultado = obtener_fecha_foto(metadatos)

  assert resultado == datetime(2026, 4, 19, 21, 56, 33)

def test_obtener_fecha_foto_sin_fecha():
  metadatos = {}

  resultado = obtener_fecha_foto(metadatos)

  assert resultado is None

def test_copiar_fotografia(tmp_path):
  carpeta_salida = tmp_path / "salida"
  carpeta_salida.mkdir()

  ruta_origen = tmp_path / "foto.jpg"
  ruta_origen.write_bytes(b"contenido de prueba")

  nombre_nuevo = "2026-08-01_15-42-18.jpg"

  ruta_destino = copiar_fotografia(
    ruta_origen,
    carpeta_salida,
    nombre_nuevo
  )

  assert ruta_destino.exists()
  assert ruta_destino.name == nombre_nuevo
  assert ruta_destino.read_bytes() == b"contenido de prueba"

  assert ruta_origen.exists()
  assert ruta_origen.read_bytes() == b"contenido de prueba"