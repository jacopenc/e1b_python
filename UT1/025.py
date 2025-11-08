import subprocess

carpeta = "mi_carpeta"

# Borrar carpeta y todo su contenido **pidiendo confirmación**
subprocess.run([
    "cmd",       # Llama al intérprete de comandos de Windows
    "/c",        # Ejecuta el comando y luego sale
    "rmdir",
    "/s",        # Borra todos los archivos y subcarpetas
    carpeta      # Nombre de la carpeta a eliminar
], shell=True)
