

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

    print("FECHAS EXIF")
    # print("\nFECHAS EXIF")
    print("-" * 40)

    for nombre, valor in fechas.items():

        if valor is None:
            print(f"{nombre}: NO DISPONIBLE")
        else:
            print(f"{nombre}: {valor}")

def mostrar_fecha_seleccionada(fecha):
    """Muestra la fecha seleccionada para la fotografía."""


    print("=" * 60)
    print("FECHA SELECCIONADA")
    # print("\nFECHA SELECCIONADA")
    print("-" * 40)

    if fecha is None:
        print("Fecha: NO DISPONIBLE")
        print("*" * 60)
        print()
    else:
        print(f"Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        print("*" * 60)
        print()

def mostrar_resumen(resumen):
    """ Muestra un resumen del procesamiento de fotografías """

    print("\n" + "=" * 60)
    print("RESUMEN DEL PROCESO")
    print("=" * 60)

    print(f"Fotografías encontradas: {resumen['total']}")
    print(f"Fotografías con fecha:   {resumen['con_fecha']}")
    print(f"Fotografías sin fecha:   {resumen['sin_fecha']}")
    print(f"Fotografías sin EXIF:    {resumen['sin_exif']}")
    print(f"Fotografías copiadas:    {resumen['copiadas']}")

    if resumen["fotos_sin_exif"]:
        print("\nFOTOGRAFÍAS SIN EXIF")
        print("-" * 60)

        for nombre in resumen["fotos_sin_exif"]:
            print(f"- {nombre}")

    if resumen["fotos_sin_fecha"]:
        print("\nFOTOGRAFÍAS SIN FECHA")
        print("-" * 60) 

        for nombre in resumen["fotos_sin_fecha"]:
            print(f"- {nombre}")

    print("=" * 60)
    print("Proceso finalizado")
    print("=" * 60)

def crear_resumen(total):
  """ Crea la estructura inicial del resumen del procesamiento """

  return {
    "total": total,
    "con_fecha": 0,
    "sin_fecha": 0,
    "sin_exif": 0,
    "copiadas": 0,
    "fotos_sin_exif": [],
    "fotos_sin_fecha": [],
    "fotos_copiadas": []
  }

def actualizar_resumen(resumen, estado, nombre_foto):
    """ Actualiza el resujmen según el estado de una fotografía. """

    if estado == "SIN_EXIF":
        resumen["sin_exif"] += 1
        resumen["fotos_sin_exif"].append(nombre_foto)

    elif estado == "SIN_FECHA":
        resumen["sin_fecha"] += 1
        resumen["fotos_sin_fecha"].append(nombre_foto)

    elif estado == "CON_FECHA":
        resumen["con_fecha"] += 1

def registrar_fotografia_copiada(resumen, nombre_foto):
    """ Registra una fotografía copiada correctamente. """

    resumen["copiadas"] += 1
    resumen["fotos_copiadas"].append(nombre_foto)

