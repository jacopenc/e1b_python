import os
import platform

# Información del sistema
so = platform.system()
print("Sistema operativo:", so)
print("Versión:", platform.version())

# Guardar directorio original
dir_original = os.getcwd()
print("Directorio original:", dir_original)

# Crear directorio principal "proyecto"
dir_proyecto = "proyecto"
if not os.path.exists(dir_proyecto):
    os.mkdir(dir_proyecto)
    print("Directorio '" + dir_proyecto + "' creado.")
else:
    print("Directorio '" + dir_proyecto + "' ya existe.")

# Entrar a "proyecto"
os.chdir(dir_proyecto)
print("Directorio actual:", os.getcwd())

# Crear subdirectorio "docs"
dir_docs = "docs"
if not os.path.exists(dir_docs):
    os.mkdir(dir_docs)
    print("Subdirectorio '" + dir_docs + "' creado dentro de '" + dir_proyecto + "'.")
else:
    print("Subdirectorio '" + dir_docs + "' ya existe.")

# Crear subdirectorio "src"
dir_src = "src"
if not os.path.exists(dir_src):
    os.mkdir(dir_src)
    print("Subdirectorio '" + dir_src + "' creado dentro de '" + dir_proyecto + "'.")
else:
    print("Subdirectorio '" + dir_src + "' ya existe.")

# Entrar en "src" y crear "modulos"
os.chdir(dir_src)
print("Directorio actual:", os.getcwd())

dir_modulos = "modulos"
if not os.path.exists(dir_modulos):
    os.mkdir(dir_modulos)
    print("Subdirectorio '" + dir_modulos + "' creado dentro de '" + dir_src + "'.")
else:
    print("Subdirectorio '" + dir_modulos + "' ya existe.")

# Volver al directorio original
os.chdir(dir_original)
print("Volvemos al directorio original:", os.getcwd())

# Listado recursivo del directorio "proyecto"
print("\n Listado recursivo de '" + dir_proyecto )
if so == "Windows":
    os.system("dir /s")
elif so in ("Linux", "Darwin"):
    os.system("ls -lR")
else:
    print("Sistema operativo no reconocido")

print("\nEjecución completada.")
