import subprocess

fichero = "salida.txt"

# Ejecutamos el comando para borrar un archivo en Windows
subprocess.run([
    "cmd",       # Llama al intérprete de comandos de Windows
    "/c",        # Ejecuta el siguiente comando y luego sale
    "del",       # Comando de Windows para eliminar un archivo
    fichero      # Nombre del archivo a eliminar
], shell=True)  # shell=True permite ejecutar comandos de shell en Windows
