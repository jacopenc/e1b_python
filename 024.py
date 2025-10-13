import subprocess

carpeta = "mi_carpeta"

# Borrar carpeta y todo su contenido sin pedir confirmación
subprocess.run([
    "cmd",
    "/c",
    "rmdir",
    "/s",        # Borra todos los archivos y subcarpetas
    "/q",        # No pide confirmación
    carpeta
], shell=True)
