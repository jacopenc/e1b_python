numero_secreto = 7
intentos_restantes = 5  # Número máximo de intentos
jugando = True  # Variable de control del bucle

while jugando:
    adivinanza = int(input("Adivina el número (1-10): "))
    
    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Lo adivinaste!")
        jugando = False  # Salimos del bucle cambiando la variable
    else:
        intentos_restantes -= 1
        if intentos_restantes == 0:
            print("Se te acabaron los intentos. El número era", numero_secreto)
            jugando = False  # Salimos del bucle
        else:
            print("Número incorrecto.")
            print("Te quedan", intentos_restantes, "intento(s).")
