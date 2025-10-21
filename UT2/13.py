import subprocess

print("Elige tu sistema operativo:")
print("1. Windows")
print("2. Linux / macOS")

opcion = input("Escribe el número de tu elección: ")

match opcion:
    case "1":
        print("Has elegido Windows")
        comando = input("Escribe un comando de Windows para ejecutar: ")
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("Salida del comando:")
            print(resultado.stdout)
        except Exception as e:
            print("Ocurrió un error:", e)
    case "2":
        print("Has elegido Linux / macOS")
        comando = input("Escribe un comando de Linux/macOS para ejecutar: ")
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("Salida del comando:")
            print(resultado.stdout)
        except Exception as e:
            print("Ocurrió un error:", e)
    case _:
        print("Opción no válida")
