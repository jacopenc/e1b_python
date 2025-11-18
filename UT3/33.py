# Diccionario de ejemplo
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Eliminar el elemento con clave 'edad'
#Si la clave no existe, se generará un KeyError. 
# Para evitarlo, verifica si la clave está presente
if 'edad' in mi_diccionario:
    del mi_diccionario['edad']

print(mi_diccionario)
# Salida: {'nombre': 'Juan', 'ciudad': 'Madrid'}