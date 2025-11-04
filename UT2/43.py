import os

# Pedir nombre de la carpeta principal
ruta_completa = input("Escribe el nombre de la carpeta principal: ")
os.makedirs(ruta_completa, exist_ok=True)
print("Carpeta principal creada:", ruta_completa, "\n")

# Crear niveles adicionales con while
while True:
    nivel = input("Escribe el nombre de un subnivel (o escribe 'salir' para terminar): ")
    if nivel.lower() == "salir":
        break
    ruta_completa += "/" + nivel
    os.makedirs(ruta_completa, exist_ok=True)
    print("Nivel creado:", ruta_completa)

print("\nRuta final completa creada:", ruta_completa, "\n")

# Bucle interactivo para archivos
while True:
    print("Opciones:")
    print("1. Crear o añadir archivo")
    print("2. Listar archivos de la carpeta final")
    print("3. Renombrar archivo")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nombre_archivo = input("Nombre del archivo: ")
        ruta_archivo = ruta_completa + "/" + nombre_archivo

        # Comprobar si existe el archivo
        if os.path.exists(ruta_archivo):
            modo_input = input("El archivo ya existe. Escribe 's' para sobrescribir o 'a' para añadir: ").lower()
            if modo_input == "s":
                modo = "w"
            elif modo_input == "a":
                modo = "a"
            else:
                print("Opción no válida, se cancela la acción.\n")
                continue
        else:
            modo = "w"

        # Crear o añadir contenido al archivo
        with open(ruta_archivo, modo) as archivo:
            contenido = input("Escribe el contenido del archivo: ")
            archivo.write(contenido + "\n")
        print("Archivo guardado correctamente.\n")

    elif opcion == "2":
        # Listar archivos y carpetas del nivel final
        print("Contenido de la carpeta final:", os.listdir(ruta_completa))

    elif opcion == "3":
        ruta_vieja = input("Ruta completa del archivo a renombrar: ")
        if not os.path.exists(ruta_vieja):
            print("El archivo no existe.\n")
            continue
        ruta_nueva = input("Introduce el nuevo nombre del archivo (con ruta si quieres cambiar de carpeta): ")
        os.rename(ruta_vieja, ruta_nueva)
        print("Archivo renombrado correctamente.\n")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida, intenta de nuevo.\n")
