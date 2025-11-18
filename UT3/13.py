numero_secreto = 7
intentos_restantes = 5  # Número máximo de intentos

while intentos_restantes > 0:
    adivinanza = int(input("Adivina el número (1-10): "))
    
    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Lo adivinaste!")
        break
    else:
        intentos_restantes -= 1
        print("Número incorrecto.")
        print("Te quedan", intentos_restantes, "intento(s).")

if intentos_restantes == 0:
    print("Se te acabaron los intentos. El número era", numero_secreto)
