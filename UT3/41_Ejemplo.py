import os
import platform
import time

# Usando 'platform' para mostrar información del sistema
print("Información del sistema:")
print("Sistema operativo:", platform.system())
print("Nombre del equipo:", platform.node())
print("Versión:", platform.version())
print("Procesador:", platform.processor())
print()

# Usando 'os' para listar archivos de un directorio
directorio = "."  # Directorio actual
# os.getcwd()  # Obtiene la ruta del directorio actual
archivos = os.listdir(directorio)

print("Archivos en el directorio actual (usando for):")
for archivo in archivos:
    print("-", archivo)

print()#sin nada dentro agrega un salto de línea

# Usando while para contar los archivos listados
print("Contando archivos con while:")
contador = 0
while contador < len(archivos):
    print(contador + 1, archivos[contador])  # Usando comas en lugar de f-string
    contador += 1
    time.sleep(0.2)  # Pequeña pausa para ver el conteo
