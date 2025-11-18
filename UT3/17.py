numero_secreto = 7
intentos_restantes = 5
entrada = ""  # Inicializamos la variable

while entrada.lower() != "salir" and intentos_restantes > 0:
    entrada = input("Adivina el número (1-10) o escribe 'salir' para terminar: ")
    
    if entrada.lower() == "salir":
        print("Has decidido salir del juego.")
    elif entrada.isdigit():  # Verificamos que sea un número
        adivinanza = int(entrada)
        if adivinanza == numero_secreto:
            print("¡Correcto! ¡Lo adivinaste!")
            break  # Solo salimos si acierta
        else:
            intentos_restantes -= 1
            if intentos_restantes > 0:
                print("Número incorrecto. Te quedan", intentos_restantes, "intento(s).")
            else:
                print("Se te acabaron los intentos. El número era", numero_secreto)
    else:
        print("Entrada inválida. Escribe un número o 'salir'.")
