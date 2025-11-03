import os
import platform

# Información del sistema
so = platform.system()
print("Sistema operativo:", so)
print("Versión:", platform.version())

# Nombre del directorio a eliminar
dir_a_eliminar = "directorio_vacio"

# Comprobar si existe y eliminar
if os.path.exists(dir_a_eliminar):
   
    os.rmdir(dir_a_eliminar) 
    # PREGUNTAR ALUMNADO QUE HACER ??????
    # Solo funciona si el directorio está vacío
    
    print("Directorio '" + dir_a_eliminar + "' eliminado correctamente.")
  
else:
    print("El directorio '" + dir_a_eliminar + "' no existe.")

print("\nEjecución completada.")
