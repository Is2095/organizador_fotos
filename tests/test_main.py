from pathlib import Path

from PIL import Image

from src.main import main

def test_main_procesa_fotografias(tmp_path, monkeypatch):
  carpeta_entrada = tmp_path / "fotos_entrada"
  carpeta_salida = tmp_path / "fotos_salida"

  carpeta_entrada.mkdir()

  # Fotografía con fecha EXIF
  ruta_foto_con_fecha = carpeta_entrada / "foto_con_fecha.jpg"

  imagen = Image.new("RGB", (100, 100))

  exif = imagen.getexif()
  exif[306] = "2026:08:01 15:42:18"

  imagen.save(
    ruta_foto_con_fecha,
    exif=exif.tobytes()
  )

  # Fotografía sin EXIF
  ruta_foto_sin_exif = carpeta_entrada / "foto_sin_exif.jpg"

  imagen_sin_exif = Image.new("RGB", (100, 100))
  imagen_sin_exif.save(ruta_foto_sin_exif)

  # Archivo que no es fotografía
  archivo_txt = carpeta_entrada / "documento.txt"
  archivo_txt.write_text("archivo de prueba")

  # Reemplazamos las carpetas reales del programa
  monkeypatch.setattr(
    "src.main.CARPETA_ENTRADA",
    carpeta_entrada
  )

  monkeypatch.setattr(
    "src.main.CARPETA_SALIDA",
    carpeta_salida
  )

  main()

  # La carpeta de salida debe existir
  assert carpeta_salida.exists()

  # La fotografía con fecha debe haberse copiado
  foto_destino = (
    carpeta_salida /
    "2026-08-01_15-42-18.jpg"
  )

  assert foto_destino.exists()

  # La fotografía sin EXIF no debe copiarse
  assert not (
    carpeta_salida /
    "foto_sin_exif.jpg"
  ).exists()

  # El archivo de texto tampoco debe copiarse
  assert not (
    carpeta_salida /
    "documento.txt"
  ).exists()

  # El original debe seguir existiendo
  assert ruta_foto_con_fecha.exists()
  assert ruta_foto_sin_exif.exists()

def test_main_cuando_no_existe_carpeta_entrada(tmp_path, monkeypatch, capsys):
    carpeta_entrada = tmp_path / "fotos_entrada"
    carpeta_salida = tmp_path / "fotos_salida"

    monkeypatch.setattr(
        "src.main.CARPETA_ENTRADA",
        carpeta_entrada
    )

    monkeypatch.setattr(
        "src.main.CARPETA_SALIDA",
        carpeta_salida
    )

    main()

    salida = capsys.readouterr().out

    assert "La carpeta fotos_entrada no existe." in salida

    assert not carpeta_salida.exists()


def test_main_cuando_no_hay_fotografias(tmp_path, monkeypatch, capsys):
  carpeta_entrada = tmp_path / "fotos_entrada"
  carpeta_salida = tmp_path / "fotos_salida"

  carpeta_entrada.mkdir()

  monkeypatch.setattr(
    "src.main.CARPETA_ENTRADA",
    carpeta_entrada
  )

  monkeypatch.setattr(
    "src.main.CARPETA_SALIDA",
    carpeta_salida
  )

  main()

  salida = capsys.readouterr().out

  assert "No hay fotografías en fotos_entrada." in salida

  assert not carpeta_salida.exists()
  