import os


archivo = open("ejemplo.txt", "w")  # Modo escritura
archivo.write("Hola, esto es un archivo de ejemplo.\n")
archivo.write("Segunda línea de texto.")
archivo.close()  # Cerrar para guardar los cambios

print("Archivo creado con contenido.")
