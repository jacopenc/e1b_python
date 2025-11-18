numero_secreto = 7
max_intentos = 3
intentos = 0

while intentos < max_intentos:
    adivinanza = int(input("Adivina el número (1-10): "))
    intentos += 1

    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Lo adivinaste en", intentos, "intento(s)!")
        break
    else:
        print("Número incorrecto.")
        print("Te quedan", max_intentos - intentos, "intento(s).")

if intentos == max_intentos and adivinanza != numero_secreto:
    print("Se te acabaron los intentos. El número era", numero_secreto)
