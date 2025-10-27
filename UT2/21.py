import platform

respuesta = input("¿Quieres ver la información de tu sistema? (si/no): ")

if respuesta.lower() == "si":
    # Versión del sistema operativo
    version = platform.version()
    print("Versión del sistema:", version)

    # Nombre de la máquina / computadora
    nombre_maquina = platform.node()
    print("Nombre de la máquina:", nombre_maquina)

    # Versión de Python
    python_ver = platform.python_version()
    print("Versión de Python:", python_ver)

    # Arquitectura del sistema (32 o 64 bits)
    arquitectura = platform.architecture()[0]

    # Información completa del sistema
    info = platform.uname()
    print("Información del sistema:")
    print(info)

    # Detectar el sistema operativo
    sistema = platform.system()
    if sistema == "Windows":
        print("Estás usando Windows")      
    elif sistema == "Linux":
        print("Estás usando Linux")    
    elif sistema == "Darwin":
        print("Estás usando macOS")     
    else:
        print("Sistema operativo desconocido o no identificado.")
    # Mostrar tipo de arquitectura
    if "64" in arquitectura:
        print("Sistema de 64 bits (más moderno y potente)")
    elif "32" in arquitectura:
        print("Sistema de 32 bits (más antiguo)")
    else:
        print("Arquitectura no reconocida.")
else:
    print("De acuerdo, no se mostrará la información del sistema.")
