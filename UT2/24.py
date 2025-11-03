import os
import platform

# Muestra información del sistema
print("=== Información del sistema ===")
print("Sistema operativo:", platform.system())
print("Versión:", platform.version())
print("===============================")

# Detecta el sistema operativo
so = platform.system()

# Dependiendo del sistema, ejecuta distintas órdenes
if so == "Windows":
    print("Estás en Windows")
    
    # Listar archivos usando comando de Windows
    os.system("dir")
    
  
elif so == "Linux":
    print("Estás en Linux")
    
    # Listar archivos usando comando de Linux
    os.system("ls -l")
    
     
elif so == "Darwin":   # macOS
    print("Estás en macOS")
    
    os.system("ls -l")
    
else:
    print("Sistema operativo no reconocido")

print("\nEjecución completada.")
