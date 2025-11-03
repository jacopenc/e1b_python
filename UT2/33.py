import os
dir_proyecto="proyectoAsir"

print("Contenido del directorio actual:")
print(os.listdir("."))

if not os.path.exists(dir_proyecto):
    os.mkdir(dir_proyecto)
    print("Directorio '" + dir_proyecto + "' creado.")
else:
    print("Directorio '" + dir_proyecto + "' ya existe.")

# Cambiar al nuevo directorio
os.chdir(dir_proyecto)
#Creo nuevo directorio
dir_ejercicio="ejercicio"
if not os.path.exists(dir_ejercicio):
    os.mkdir(dir_ejercicio)
    print("Directorio '" + dir_ejercicio + "' creado.")
else:
    print("Directorio '" + dir_ejercicio + "' ya existe.")


# Volver al directorio anterior (al nivel donde está dir_proyecto)
os.chdir("..")
# Listar contenido de dir_ejercicio usando ruta relativa directa
print(os.listdir("proyectoAsir/ejercicio"))

# Ruta absoluta
# Windows
#  print(os.listdir("C:/Users/jmacosta/proyectoAsir/ejercicio"))

# Linux/macOS
#  print(os.listdir("/home/jmacosta/proyectoAsir/ejercicio"))


