import subprocess

try:
    proceso = subprocess.run(
        ["powershell", "Get-ChildItem"],  # equivalente de dir en PowerShell
        capture_output=True,
        text=True
    )
    print("Salida estándar:")
    print(proceso.stdout)
    print("Salida de error:")
    print(proceso.stderr)
except Exception as e:
    print("Ocurrió un error:", e)
