from src.procesador import (
  procesar_fotografia,
  obtener_fotografias
)

# def test_procesar_fotografia_sin_exif(monkeypatch, tmp_path):
#   ruta_foto = tmp_path / "foto.jpg"
#   ruta_foto.touch()

#   monkeypatch.setattr(
#     "src.procesador.leer_exif",
#     lambda ruta: {}
#   )

#   resultado = procesar_fotografia(ruta_foto)

#   assert resultado["estado"] == "SIN_EXIF"
#   assert resultado["fecha"] is None
#   assert resultado["metadatos"] == {}

# def test_procesar_fotografia_sin_fecha(monkeypatch, tmp_path):
#   ruta_foto = tmp_path / "foto.jpg"
#   ruta_foto.touch()

#   monkeypatch.setattr(
#     "src.procesador.leer_exif",
#     lambda ruta: {
#       "Make": "Motorola",
#       "Model": "moto g86 5G"
#     }
#   )

#   resultado = procesar_fotografia(ruta_foto)

#   assert resultado["estado"] == "SIN_FECHA"
#   assert resultado["fecha"] is None
#   assert resultado["metadatos"]["Make"] == "Motorola"

# def test_procesar_fotografia_con_fecha(monkeypatch, tmp_path):
#   ruta_foto = tmp_path / "foto.jpg"
#   ruta_foto.touch()

#   monkeypatch.setattr(
#     "src.procesador.leer_exif",
#     lambda ruta: {
#       "Make": "Motorola",
#       "Model": "moto g86 5G",
#       "DateTime": "2026:08:01 15:42:18"
#     }
#   )

#   resultado = procesar_fotografia(ruta_foto)

#   assert resultado["estado"] == "CON_FECHA"
#   assert resultado["fecha"].year == 2026
#   assert resultado["fecha"].month == 8
#   assert resultado["fecha"].day == 1

def test_obtener_fotografias_encuentra_fotos(tmp_path):
  (tmp_path / "foto1.jpg").touch()
  (tmp_path / "foto2.jpeg").touch()
  (tmp_path / "foto3.png").touch()

  resultado = obtener_fotografias(tmp_path)

  assert len(resultado) == 3

def test_obtener_fotografias_ignora_archivos_no_validos(tmp_path):
  (tmp_path / "foto.jpg").touch()
  (tmp_path / "documento.txt").touch()
  (tmp_path / "archivo.pdf").touch()

  resultado = obtener_fotografias(tmp_path)

  assert len(resultado) == 1
  assert resultado[0].name == "foto.jpg"

def test_obtener_fotografias_ignora_carpetas(tmp_path):
  (tmp_path / "foto.jpg").touch()
  (tmp_path / "carpeta").mkdir()

  resultado = obtener_fotografias(tmp_path)

  assert len(resultado) == 1
  assert resultado[0].name == "foto.jpg"
