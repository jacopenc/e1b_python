import subprocess

carpeta = "mi_carpeta"

# Borrar carpeta vacía
subprocess.run([
    "cmd",       # Llama al intérprete de comandos de Windows
    "/c",        # Ejecuta el comando y luego sale
    "rmdir",     # Comando para eliminar carpeta
    carpeta
], shell=True)
