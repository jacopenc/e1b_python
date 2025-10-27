import platform

print("BIENVENIDO AL CONSULTOR DE INFORMACIÓN DEL SISTEMA")

while True:
    respuesta = input("\n¿Quieres ver la información de tu sistema? (si/no/salir): ").lower()

    if respuesta == "si":
        # Mostrar el menú de opciones
        print("\n¿Qué información quieres ver?")
        print("1. Versión del sistema operativo")
        print("2. Nombre de la máquina")
        print("3. Versión de Python")
        print("4. Arquitectura del sistema")
        print("5. Toda la información")
        print("6. Salir del programa")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            print("Versión del sistema:", platform.version())

        elif opcion == "2":
            print("Nombre de la máquina:", platform.node())

        elif opcion == "3":
            print("Versión de Python:", platform.python_version())

        elif opcion == "4":
            print("Arquitectura del sistema:", platform.architecture()[0])

        elif opcion == "5":
            print("Información completa del sistema:")
            print(platform.uname())

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta pronto!")
            break  # Sale del bucle

        else:
            print("Opción no válida. Por favor, elige entre 1 y 6.")

    elif respuesta == "no":
        print("De acuerdo, no se mostrará la información del sistema. ")

    elif respuesta == "salir":
        print("Programa finalizado. ¡Hasta pronto!")
        break  # Sale del bucle

    else:
        print("Respuesta no reconocida. Escribe 'si', 'no' o 'salir'.")
