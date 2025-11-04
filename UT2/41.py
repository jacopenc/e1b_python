import os

# Tamaño de un archivo en bytes
print(os.path.getsize("archivo.txt"))

# Comprobar si es archivo o directorio
print(os.path.isfile("archivo.txt"))   # True si es archivo
print(os.path.isdir("carpeta"))        # True si es carpeta

# Última fecha de modificación
print(os.path.getmtime("archivo.txt"))

# Última fecha de acceso
print(os.path.getatime("archivo.txt"))
