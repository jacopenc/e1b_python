import os
import platform

# Información del sistema
so = platform.system()
print("Sistema operativo:", so)
print("Versión:", platform.version())

# Nombres de los directorios
dir_padre = "directorio_padre"
dir_hijo = "subdirectorio"

# Crear directorio padre si no existe
if not os.path.exists(dir_padre):
    os.mkdir(dir_padre)
    print("Directorio '" + dir_padre + "' creado.")
else:
    print("Directorio '" + dir_padre + "' ya existe.")

# Entrar al directorio padre
os.chdir(dir_padre)
print("Directorio actual:", os.getcwd())

# Crear subdirectorio dentro del padre
if not os.path.exists(dir_hijo):
    os.mkdir(dir_hijo)
    print("Subdirectorio '" + dir_hijo + "' creado dentro de '" + dir_padre + "'.")
else:
    print("Subdirectorio '" + dir_hijo + "' ya existe.")

# Volver al directorio anterior al padre
os.chdir("..")
print("Ahora estamos en:", os.getcwd())

# Listado recursivo del directorio padre
print("\n=== Listado recursivo de '" + dir_padre + "' ===")
if so == "Windows":
    os.system("dir /s")
elif so in ("Linux", "Darwin"):
    os.system("ls -lR")
else:
    print("Sistema operativo no reconocido")

print("\nEjecución completada.")
