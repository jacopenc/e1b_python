import os

# ---------------------------------------------------------
# Crear la carpeta principal
# ---------------------------------------------------------
def crear_carpeta_principal():
    ruta = input("Escribe el nombre de la carpeta principal: ")
    os.makedirs(ruta, exist_ok=True)
    print("Carpeta principal creada:", ruta, "\n")
    return ruta


# ---------------------------------------------------------
# Crear niveles adicionales
# ---------------------------------------------------------
def crear_subniveles(ruta):
    ruta_actual = ruta
    while True:
        nivel = input("Escribe el nombre de un subnivel (o escribe 'salir' para terminar): ")
        if nivel.lower() == "salir":
            break

        ruta_actual = os.path.join(ruta_actual, nivel)
        os.makedirs(ruta_actual, exist_ok=True)
        print("Nivel creado:", ruta_actual)

    print("\nRuta final completa creada:", ruta_actual, "\n")
    return ruta_actual


# ---------------------------------------------------------
# Crear o añadir contenido a un archivo
# ---------------------------------------------------------
def crear_o_añadir_archivo(ruta_final):
    nombre_archivo = input("Nombre del archivo: ")
    ruta_archivo = os.path.join(ruta_final, nombre_archivo)

    # Verificar existencia
    if os.path.exists(ruta_archivo):
        modo_input = input("El archivo ya existe. Escribe 's' para sobrescribir o 'a' para añadir: ").lower()
        if modo_input == "s":
            modo = "w"
        elif modo_input == "a":
            modo = "a"
        else:
            print("Opción no válida, acción cancelada.\n")
            return
    else:
        modo = "w"

    # Escribir contenido
    with open(ruta_archivo, modo) as archivo:
        contenido = input("Escribe el contenido del archivo: ")
        archivo.write(contenido + "\n")

    print("Archivo guardado correctamente.\n")


# ---------------------------------------------------------
# Listar contenido del último nivel
# ---------------------------------------------------------
def listar_contenido(ruta_final):
    print("Contenido de la carpeta final:", os.listdir(ruta_final), "\n")


# ---------------------------------------------------------
# Renombrar un archivo
# ---------------------------------------------------------
def renombrar_archivo():
    ruta_vieja = input("Ruta completa del archivo a renombrar: ")
    if not os.path.exists(ruta_vieja):
        print("El archivo no existe.\n")
        return

    ruta_nueva = input("Introduce el nuevo nombre del archivo (con ruta si quieres cambiar de carpeta): ")
    os.rename(ruta_vieja, ruta_nueva)
    print("Archivo renombrado correctamente.\n")


# ---------------------------------------------------------
# Menú principal
# ---------------------------------------------------------
def menu_archivos(ruta_final):
    while True:
        print("Opciones:")
        print("1. Crear o añadir archivo")
        print("2. Listar archivos de la carpeta final")
        print("3. Renombrar archivo")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            crear_o_añadir_archivo(ruta_final)
        elif opcion == "2":
            listar_contenido(ruta_final)
        elif opcion == "3":
            renombrar_archivo()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")


# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    carpeta_principal = crear_carpeta_principal()
    ruta_final = crear_subniveles(carpeta_principal)
    menu_archivos(ruta_final)


# Ejecutar programa
if __name__ == "__main__":
    main()
