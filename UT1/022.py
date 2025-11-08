import subprocess
carpeta = "mi_carpeta"

# Crear una carpeta
subprocess.run([
    "cmd",
    "/c",
    "mkdir",     # Comando para crear carpeta
    carpeta
], shell=True)
