import subprocess  # Importamos el módulo subprocess para ejecutar comandos del sistema

try:
    # Ejecutamos el comando 'dir' usando cmd.exe
    proceso = subprocess.run(
        "dir",          # Comando a ejecutar, en este caso 'dir' para listar archivos y carpetas
        shell=True,     # Usamos 'shell=True' para que 'cmd.exe' interprete el comando
        capture_output=True,  # Capturamos la salida estándar (stdout) y de error (stderr)
        text=True       # Indicamos que la salida debe ser tratada como texto (str), no como bytes
    )

    # Mostramos la salida estándar del comando
    print("Salida estándar:")
    print(proceso.stdout)

    # Mostramos la salida de error estándar del comando (si la hay)
    print("Salida de error:")
    print(proceso.stderr)

except Exception as e:
    # Si ocurre algún error durante la ejecución del comando, lo capturamos y mostramos
    print("Ocurrió un error:", e)
