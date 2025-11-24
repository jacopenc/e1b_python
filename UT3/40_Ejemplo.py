import os
import platform
import time

# Información del sistema
print("=== Información del Sistema ===")
print("Sistema operativo:", platform.system())
print("Nombre del equipo:", platform.node())
print("Versión:", platform.version())
print("Procesador:", platform.processor())
print()

# Directorio a explorar
directorio = "."  # Directorio actual
archivos = os.listdir(directorio)

# Mostrar archivos con su tamaño (en bytes) usando for
print("=== Archivos y sus tamaños ===")
for archivo in archivos:
    ruta_completa = os.path.join(directorio, archivo)
    if os.path.isfile(ruta_completa):  # Solo archivos, no carpetas
        tamaño = os.path.getsize(ruta_completa)
        print(archivo, "-", tamaño, "bytes")

print()

# Mostrar archivos y su tipo usando while
print("=== Archivos y su tipo (extensión) ===")
contador = 0
while contador < len(archivos):
    archivo = archivos[contador]
    if os.path.isfile(os.path.join(directorio, archivo)):
        extension = os.path.splitext(archivo)[1]  # Obtener extensión
        print(archivo, "es del tipo", extension)
    contador += 1
    time.sleep(0.1)  # Pequeña pausa para ver el listado
