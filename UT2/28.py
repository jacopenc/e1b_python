import os
import platform

# Información del sistema
so = platform.system()
print("Sistema operativo:", so)
print("Versión:", platform.version())

# Nombre del directorio
nuevo_dir = "directorio_vacio"

# Crear el directorio si no existe
if not os.path.exists(nuevo_dir):
    os.mkdir(nuevo_dir)
    print("\nDirectorio '" + nuevo_dir + "' creado correctamente.")
else:
    print("\nEl directorio '" + nuevo_dir + "' ya existe.")

# Cambiar al nuevo directorio
os.chdir(nuevo_dir)
print("Directorio actual:", os.getcwd())

# Listar contenido (vacío)
print("\n=== Contenido del directorio ===")
if so == "Windows":
    os.system("dir")
elif so in ("Linux", "Darwin"):
    os.system("ls -l")
else:
    print("Sistema operativo no reconocido")

print("\nEjecución completada.")
