import os
# Crear directorio
os.mkdir("nueva_carpeta")

# Crear directorio de manera recursiva
# Crea carpetas anidadas
os.makedirs("carpeta_principal/subcarpeta/nivel2/nivel3")

#Python intenta crear toda la ruta y si alguna carpeta intermedia ya existe, falla.
#Error: FileExistsError

os.makedirs("carpeta_principal/subcarpeta", exist_ok=True)
#Solo crea las carpetas que no existan

# Eliminar directorio
os.rmdir("nueva_carpeta")

# Eliminar carpetas recursivamente
import shutil
shutil.rmtree("carpeta_principal")

# Renombrar archivo o carpeta
os.rename("viejo.txt", "nuevo.txt")
