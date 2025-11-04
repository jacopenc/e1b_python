import os

nombre_archivo = "ejemplo.txt"

# Comprobar si el archivo existe
if os.path.exists(nombre_archivo):
    print("El archivo ya existe.")
    opcion = input("Escribe 's' para sobrescribir o 'a' para añadir al final: ").lower()
    if opcion == "s":
        modo = "w"
        print("El archivo será sobrescrito.")
    elif opcion == "a":
        modo = "a"
        print("El contenido se añadirá al final del archivo.")
    else:
        print("Opción no válida. Saliendo...")
        exit()
else:
    modo = "w"  # Si no existe, se crea automáticamente
    print("El archivo no existe, se creará uno nuevo.")

# Abrir el archivo usando 'with', que cierra automáticamente
with open(nombre_archivo, modo) as archivo:
    #Cierra automáticamente el archivo, no necesitas archivo.close()
    archivo.write("Esta es una línea de ejemplo.\n")

print("Operación realizada correctamente.")
