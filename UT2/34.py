import os

# Crear un nuevo directorio
nombre_directorio = "carpeta_original"

# Comprobamos si no existe antes de crearlo
if not os.path.exists(nombre_directorio):
    os.mkdir(nombre_directorio)
    print("Directorio '" + nombre_directorio + "' creado correctamente.")
else:
    print("El directorio '" + nombre_directorio + "' ya existe.")

# Nuevo nombre para el directorio
nuevo_nombre = "carpeta_renombrada"

# Renombramos el directorio
os.rename(nombre_directorio, nuevo_nombre)
print("Directorio renombrado a '" + nuevo_nombre + "'.")
