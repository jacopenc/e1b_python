numero_secreto = 7
intentos_restantes = 5  # Número máximo de intentos

while True:
    adivinanza = int(input("Adivina el número (1-10): "))
    
    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Lo adivinaste!")
        break  # Salimos del bucle si acierta
    
    intentos_restantes -= 1  # Restamos un intento
    if intentos_restantes == 0:
        print("Se te acabaron los intentos. El número era", numero_secreto)
        break  # Salimos del bucle si se acaban los intentos
    
    print("Número incorrecto.")
    print("Te quedan", intentos_restantes, "intento(s).")
