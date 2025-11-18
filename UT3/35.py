personas =[
    {"id": 1, "nombre": "Ana", "edad": 25},
    {"id": 2, "nombre": "Luis", "edad": 30},
    {"id": 3, "nombre": "Marta", "edad": 28}
]

# Eliminar un diccionario conocido
dict_a_eliminar = {"id": 3, "nombre": "Marta", "edad": 28}
personas.remove(dict_a_eliminar)

print(personas)