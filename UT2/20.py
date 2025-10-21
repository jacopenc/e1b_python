import platform
import subprocess

# Detectar automáticamente el sistema operativo
sistema = platform.system()  # Devuelve "Windows", "Linux" o "Darwin" (macOS)

print("Sistema detectado:", sistema)

# Pedir al usuario un comando
comando = input("Escribe un comando para ejecutar en tu sistema: ")

# Ejecutar el comando usando subprocess según el S.O.
try:
    if sistema == "Windows":
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    elif sistema == "Linux" or sistema == "Darwin":
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    else:
        print("Sistema operativo no reconocido")
        exit()

    print("Salida del comando:")
    print(resultado.stdout)

except Exception as e:
    print("Ocurrió un error al ejecutar el comando:", e)
