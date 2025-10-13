import subprocess

resultado = subprocess.run(
    ["ls", "-l", "carpeta_inexistente"],
    capture_output=True,  # Captura stdout y stderr
    text=True
)

print("stdout:")
print(resultado.stdout)

print("stderr:")
print(resultado.stderr)
