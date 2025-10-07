try:
    # código con varios errores posibles
    numero = int("hola")
    resultado = 10 / 0
    suma = "texto" + 5
    lista = [1, 2, 3]
    valor = lista[10]
    diccionario = {"nombre": "Ana"}
    valor = diccionario["edad"]
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()

except Exception as e:
    print("Otro tipo de error:", type(e).__name__, "-", e)
else:
    print("Todo salió bien, sin errores.")
finally:
    print("Fin del manejo de errores.")
