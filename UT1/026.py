import subprocess

archivo = "archivo.txt"
# Crear un archivo vacío
f = open(archivo, "w")
f.close()  # Cerramos inmediatamente, el archivo ahora existe

# Crear una carpeta
carpeta = "mi_carpeta"
subprocess.run([
    "cmd",
    "/c",
    "mkdir",     # Comando para crear carpetas
    carpeta
], shell=True)

# Copiar el archivo dentro de la carpeta
subprocess.run([
    "cmd",
    "/c",
    "copy",      # Comando para copiar archivos
    archivo,
    carpeta      # Carpeta destino
], shell=True)

print("Archivo creado, carpeta creada y archivo copiado dentro de la carpeta")
