import os

# ---------------------------------------------------------
# Verificar si el archivo existe y decidir el modo (w/a)
# ---------------------------------------------------------
def obtener_modo_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print("El archivo ya existe.")
        opcion = input("Escribe 's' para sobrescribir o 'a' para añadir al final: ").lower()

        if opcion == "s":
            print("El archivo será sobrescrito.")
            return "w"
        elif opcion == "a":
            print("El contenido se añadirá al final del archivo.")
            return "a"
        else:
            print("Opción no válida. Saliendo...")
            exit()
    else:
        print("El archivo no existe, se creará uno nuevo.")
        return "w"


# ---------------------------------------------------------
# Escribir contenido en el archivo
# ---------------------------------------------------------
def escribir_archivo(nombre_archivo, modo, contenido):
    with open(nombre_archivo, modo) as archivo:
        archivo.write(contenido + "\n")
    print("Operación realizada correctamente.")


# ---------------------------------------------------------
# Función principal que junta todo
# ---------------------------------------------------------
def main():
    nombre_archivo = "ejemplo.txt"

    # Obtener el modo (crear, sobrescribir o añadir)
    modo = obtener_modo_archivo(nombre_archivo)

    # Escribir una línea de ejemplo
    escribir_archivo(nombre_archivo, modo, "Esta es una línea de ejemplo.")


# Ejecutar solo si es archivo principal
if __name__ == "__main__":
    main()
