import os
import platform

# Información del sistema
print("=== Información del sistema ===")
print("Sistema operativo:", platform.system())
print("Versión:", platform.version())
print("===============================")

so = platform.system()

print("\nDirectorio actual:", os.getcwd())

# Dependiendo del sistema operativo, usar comandos diferentes
if so == "Windows":
    print("\nEstás en Windows")
    
    # Listar archivos y carpetas
    os.system("dir") # os.system("dir /s /a")
   
    # Cambiar temporalmente al directorio raíz
    print("\nCambiando a C:\\ ...")
    os.chdir("C:\\")
    print("Nuevo directorio:", os.getcwd())
    os.system("dir")
    
elif so == "Linux":
    print("\nEstás en Linux")
    
    # Listar archivos y carpetas
    os.system("ls -l") # os.system("ls -la")
    
    # Cambiar temporalmente al directorio raíz
    print("\nCambiando a / ...")
    os.chdir("/")
    print("Nuevo directorio:", os.getcwd())
    os.system("ls -l")
    
elif so == "Darwin":  # macOS
    print("\nEstás en macOS")
    
    # Listar archivos y carpetas
    os.system("ls -l")
    
    # Cambiar temporalmente al directorio raíz
    print("\nCambiando a / ...")
    os.chdir("/")
    print("Nuevo directorio:", os.getcwd())
    os.system("ls -l")
    
else:
    print("Sistema operativo no reconocido 😕")

print("\nEjecución completada.")
