from pathlib import Path

from procesador import(
    obtener_fotografias, procesar_fotografias
)
from interfaz import (
   mostrar_metadatos,
   mostrar_fechas_exif,
   mostrar_fecha_seleccionada
)

CARPETA_ENTRADA = Path(__file__).resolve().parent.parent / "fotos_entrada"


def main():
    fotos = obtener_fotografias(CARPETA_ENTRADA)

    if not fotos: 
      print("No hay fotografías en fotos_entrada")
      return

    for numero, ruta_foto in enumerate(fotos, start=1):

      print("\n" + "=" * 60)
      print(f"FOTOGRAFÍA {numero} DE {len(fotos)}")
      print("=" * 60)
      print(f"Foto: {ruta_foto.name}")
      print("=" * 60)
      print()

      resultado = procesar_fotografias(ruta_foto)

      if resultado is None:
        print("La fotografía no contiene metadatos EXIF.")
        print("*" * 60)
        print()
        continue

      # metadatos = resultado["metadatos"]
      fechas = resultado["fechas"]
      fecha = resultado["fecha"]

      # mostrar_metadatos(metadatos)

      mostrar_fechas_exif(fechas)

      mostrar_fecha_seleccionada(fecha)

if __name__ == "__main__":
    main()