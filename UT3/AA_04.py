numero_secreto = 7
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (1-10): "))
    if adivinanza < numero_secreto:
        print("Demasiado bajo")
    elif adivinanza > numero_secreto:
        print("Demasiado alto")
print("¡Correcto! El número era", numero_secreto)
