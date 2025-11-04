import os
archivo = open("ejemplo.txt", "a") 
 # Modo añadir (append)
archivo.write("Nueva línea añadida.\n")
archivo.close()

print("Se añadió contenido al archivo existente.")
