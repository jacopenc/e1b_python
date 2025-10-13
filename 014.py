import subprocess

print("Ejecutando ping...")

proceso = subprocess.run(
    ["ping", "-n", "4", "host_inexistente"],  # -n para Windows
    capture_output=True,
    text=True,
    timeout=10,  # tiempo más amplio para evitar timeout prematuro
    check=False  # no lanza excepción aunque falle el comando
)

print("Código de salida:", proceso.returncode)

print("Salida estándar:")
print(proceso.stdout)

print("Salida de error:")
print(proceso.stderr)

print("Fin de ejecución")
