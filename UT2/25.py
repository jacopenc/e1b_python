import os
import platform

# Muestra información del sistema
print("=== Información del sistema ===")
print("Sistema operativo:", platform.system())
print("Versión:", platform.version())
print("===============================")

so = platform.system()

# Mostrar el directorio actual
print("\nDirectorio actual:", os.getcwd())

# Dependiendo del sistema operativo, usar distintos comandos
if so == "Windows":
    print("\nEstás en Windows")
    
    # Listar contenido del directorio actual
    os.system("dir")
    
    # Cambiar al directorio anterior
    print("\nCambiando al directorio anterior...")
    os.chdir("..")
    print("Ahora estás en:", os.getcwd())
    
    # Mostrar contenido del nuevo directorio
    os.system("dir")
    
elif so == "Linux":
    print("\nEstás en Linux")
    
    # Listar contenido del directorio actual
    os.system("ls -l")
    
    # Cambiar al directorio anterior
    print("\nCambiando al directorio anterior...")
    os.chdir("..")
    print("Ahora estás en:", os.getcwd())
    
    # Mostrar contenido del nuevo directorio
    os.system("ls -l")
    
elif so == "Darwin":  # macOS
    print("\nEstás en macOS")
    
    # Listar contenido del directorio actual
    os.system("ls -l")
    
    # Cambiar al directorio anterior
    print("\nCambiando al directorio anterior...")
    os.chdir("..")
    print("Ahora estás en:", os.getcwd())
    
    # Mostrar contenido del nuevo directorio
    os.system("ls -l")
    
else:
    print("Sistema operativo no reconocido")

print("\nEjecución completada.")
