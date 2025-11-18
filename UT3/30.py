edades = {"Ana": 25, "Jose Acosta": 30}
nombre = "Luis"

if nombre in edades:
    edades[nombre] = 35
else:
    print("No se encontró",nombre," en el diccionario.")