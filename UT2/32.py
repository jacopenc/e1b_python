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
    try:
        os.rmdir(dir_a_eliminar)  
        # Solo funciona si el directorio está vacío
        #OTRA SOLUCIÓN:  shutil.rmtree(dir_a_eliminar)  # Elimina todo el directorio y su contenido (requiere importar shutil)
        print("Directorio '" + dir_a_eliminar + "' eliminado correctamente.")   

    except OSError:  #PREGUNTA ALUMANADO , LO QUITAMOS ????????  Captura error si el directorio no está vacío o no se puede eliminar
        print("No se puede eliminar '" + dir_a_eliminar + "', no está vacío.")
else:
    print("El directorio '" + dir_a_eliminar + "' no existe.")

print("\nEjecución completada.")
