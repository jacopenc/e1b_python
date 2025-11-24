#Funciones con múltiples valores (return múltiple)
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(10, 3)
print(s, r)