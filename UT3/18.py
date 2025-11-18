numero_secreto = 7
intentos_restantes = 5
entrada = ""  # Inicializamos la variable

while entrada.lower() != "salir" and intentos_restantes > 0 and entrada != str(numero_secreto):
    entrada = input("Adivina el número (1-10) o escribe 'salir' para terminar: ")
    
    if entrada.lower() != "salir":
        if entrada == str(numero_secreto):
            print("¡Correcto! ¡Lo adivinaste!")
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print("Número incorrecto. Te quedan", intentos_restantes, "intento(s).")
            else:
                print("Se te acabaron los intentos. El número era", numero_secreto)
    else:
        print("Has decidido salir del juego.")
