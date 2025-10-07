try:
    # 1. ValueError → convertir texto a número
    numero = int("hola")
    """
    Este es un bloque de texto
    que parece un comentario,
    pero en realidad es una cadena.
    """

    # 2. ZeroDivisionError → dividir entre cero
    resultado = 10 / 0

    # 3. TypeError → sumar tipos incompatibles
    suma = "texto" + 5

    # 4. IndexError → acceder a un índice inexistente
    lista = [1, 2, 3]
    valor = lista[10]

    # 5. KeyError → acceder a una clave inexistente en un diccionario
    diccionario = {"nombre": "Ana"}
    valor = diccionario["edad"]

    # 6. FileNotFoundError → intentar abrir un archivo que no existe
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()

except ValueError as e:
    print("Error de valor:", e)
except ZeroDivisionError as e:
    print("Error de división:", e)
except TypeError as e:
    print("Error de tipo:", e)
except IndexError as e:
    print("Error de índice:", e)
except KeyError as e:
    print("Error de clave:", e)
except FileNotFoundError as e:
    print("Error de archivo:", e)
except Exception as e:
    print("Otro tipo de error:", type(e).__name__, "-", e)
else:
    print("Todo salió bien, sin errores.")
finally:
    print("Fin del manejo de errores.")
