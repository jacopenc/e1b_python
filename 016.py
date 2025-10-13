import subprocess

try:
    proceso = subprocess.run(
        ["cmd", "/c", "dir"],  # Ejecuta 'dir' a través de cmd.exe
        capture_output=True,
        text=True
    )
    print("Salida estándar:")
    print(proceso.stdout)
    print("Salida de error:")
    print(proceso.stderr)
except Exception as e:
    print("Ocurrió un error:", e)
