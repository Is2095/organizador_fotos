from pathlib import Path
from metadatos import leer_exif, obtener_fechas_exif

CARPETA_ENTRADA = Path(__file__).resolve().parent.parent / "fotos_entrada"

def mostrar_metadatos(metadatos):

   """Muestra los metadatos EXIF en pantalla."""

   for nombre, valor in metadatos.items():
      if nombre == "GPSInfo" and isinstance(valor, dict):
         print("\nGPS: ")
         for nombre_gps, valor_gps in valor.items():
            print(f" {nombre_gps}: {valor_gps}")

      else:
         print(f"{nombre}: {valor}")

def mostrar_fechas_exif(fechas):
    """Muestra las fechas disponibles en los metadatos EXIF."""

    print("\nFECHAS EXIF")
    print("-" * 40)

    for nombre, valor in fechas.items():

        if valor is None:
            print(f"{nombre}: NO DISPONIBLE")
        else:
            print(f"{nombre}: {valor}")

def main():
    fotos = list(CARPETA_ENTRADA.iterdir())

    if not fotos: 
      print("No hay fotografías en fotos_entrada")
      return

    ruta_foto = fotos[0]

    print("=" * 60)
    print("INFORMACIÓN EXIF")
    print("=" * 60)
    print(f"Foto: {ruta_foto.name}")
    print("=" * 60)

    metadatos = leer_exif(ruta_foto)

    if not metadatos:
       print("La fotografía no contiene metadatos EXIF. ")
       return

    mostrar_metadatos(metadatos)

    fechas = obtener_fechas_exif(ruta_foto)

    mostrar_fechas_exif(fechas)


if __name__ == "__main__":
    main()