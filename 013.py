import subprocess  # Importamos el módulo para ejecutar comandos del sistema operativo

try:
    # Ejecutamos el comando 'ping' para enviar 4 paquetes a google.com
    proceso = subprocess.run(
        ["ping", "-n", "4", "googe.com"],  # Comando y argumentos en forma de lista
        capture_output=True,  # Capturamos tanto la salida estándar (stdout) como la de error (stderr)
        text=True,           # Recibimos la salida como texto (cadena) en lugar de bytes
        timeout=5,           # Si el comando tarda más de 5 segundos, se interrumpe automáticamente
        check=True           # Si el comando termina con error, lanza una excepción
    )
    
    # Si todo salió bien, imprimimos la salida estándar del comando (resultado del ping)
    print(proceso.stdout)

except Exception as e:
    # Capturamos cualquier error que ocurra (timeout, error en ejecución, etc.)
    print("Ocurrió un error:", e)

