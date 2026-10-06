from pathlib import Path

from .procesador import(
    obtener_fotografias, procesar_fotografia
)
from .interfaz import (
   mostrar_fechas_exif,
   mostrar_fecha_seleccionada,
   mostrar_resumen,
   crear_resumen,
   actualizar_resumen,
   registrar_fotografia_copiada
)

from .renombrador import (
   generar_nombre_disponible,
   copiar_fotografia
)

CARPETA_ENTRADA = Path(__file__).resolve().parent.parent / "fotos_entrada"
CARPETA_SALIDA = Path(__file__).resolve().parent.parent / "fotos_salida"


def main():
    fotos = obtener_fotografias(CARPETA_ENTRADA)

    if not CARPETA_ENTRADA.exists():
       print("La carpeta fotos_entrada no existe.")
       return
    
    if not fotos: 
      print("No hay fotografías en fotos_entrada.")
      return
    
    resumen = crear_resumen(len(fotos))

    CARPETA_SALIDA.mkdir(exist_ok=True)

    for numero, ruta_foto in enumerate(fotos, start=1):

      print("\n" + "=" * 60)
      print(f"FOTOGRAFÍA {numero} DE {len(fotos)}")
      print("=" * 60)
      print(f"Foto: {ruta_foto.name}")
      print("=" * 60)
      print()

      resultado = procesar_fotografia(ruta_foto)

      estado = resultado["estado"]

      print(f"Estado: {estado}")

      actualizar_resumen(
         resumen,
         estado,
         ruta_foto.name
      )

      if estado == "SIN_EXIF":
        print("\nLa fotografía no contiene metadatos EXIF.")
        print("-" * 60)
        continue

      if estado == "SIN_FECHA":
        print("\nLa fotografía contiene EXIF, pero no tiene una fecha válida.")
        print("-" * 60)
        continue
             
      metadatos = resultado["metadatos"]
      fechas = resultado["fechas"]
      fecha = resultado["fecha"]


      # mostrar_metadatos(metadatos)

      mostrar_fechas_exif(fechas)

      mostrar_fecha_seleccionada(fecha)

      nombre_nuevo = generar_nombre_disponible(
         fecha,
         ruta_foto.suffix,
         CARPETA_SALIDA,
      )

      ruta_destino = copiar_fotografia(
         ruta_foto,
         CARPETA_SALIDA,
         nombre_nuevo
      )

      registrar_fotografia_copiada(
         resumen,
         ruta_foto.name
      )

      print(f"Fotografía copiada: {ruta_destino.name}")
      print(f"Nuevo nombre: {nombre_nuevo}")

      print("-/-" * 30)

    mostrar_resumen(resumen)



if __name__ == "__main__":
    main()

    