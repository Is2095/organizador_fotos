

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

def mostrar_fecha_seleccionada(fecha):
    """Muestra la fecha seleccionada para la fotografía."""

    print("\nFECHA SELECCIONADA")
    print("-" * 40)

    if fecha is None:
        print("Fecha: NO DISPONIBLE")
    else:
        print(f"Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")