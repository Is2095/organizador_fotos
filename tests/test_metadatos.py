from src.procesador import (
  procesar_fotografia
)

def test_procesar_fotografia_sin_exif(monkeypatch, tmp_path):
  ruta_foto = tmp_path / "foto.jpg"
  ruta_foto.touch()

  monkeypatch.setattr(
    "src.procesador.leer_exif",
    lambda ruta: {}
  )

  resultado = procesar_fotografia(ruta_foto)

  assert resultado["estado"] == "SIN_EXIF"
  assert resultado["fecha"] is None
  assert resultado["metadatos"] == {}

def test_procesar_fotografia_sin_fecha(monkeypatch, tmp_path):
  ruta_foto = tmp_path / "foto.jpg"
  ruta_foto.touch()

  monkeypatch.setattr(
    "src.procesador.leer_exif",
    lambda ruta: {
      "Make": "Motorola",
      "Model": "moto g86 5G"
    }
  )

  resultado = procesar_fotografia(ruta_foto)

  assert resultado["estado"] == "SIN_FECHA"
  assert resultado["fecha"] is None
  assert resultado["metadatos"]["Make"] == "Motorola"

def test_procesar_fotografia_con_fecha(monkeypatch, tmp_path):
  ruta_foto = tmp_path / "foto.jpg"
  ruta_foto.touch()

  monkeypatch.setattr(
    "src.procesador.leer_exif",
    lambda ruta: {
      "Make": "Motorola",
      "Model": "moto g86 5G",
      "DateTime": "2026:08:01 15:42:18"
    }
  )

  resultado = procesar_fotografia(ruta_foto)

  assert resultado["estado"] == "CON_FECHA"
  assert resultado["fecha"].year == 2026
  assert resultado["fecha"].month == 8
  assert resultado["fecha"].day == 1
