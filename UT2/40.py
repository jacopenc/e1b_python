import os

# Nombre del archivo
archivo = "documento.pdf"

# Separar nombre y extensión
nombre, extension = os.path.splitext(archivo)

# Comprobar si la extensión es .pdf (sin importar mayúsculas o minúsculas)
if extension.lower() == ".pdf":
    print("El archivo es un PDF.")
else:
    print("El archivo NO es un PDF.")
