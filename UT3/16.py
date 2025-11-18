numero_secreto = 7
entrada = ""  # Inicializamos la variable

while entrada.lower() != "salir":
    entrada = input("Adivina el número (1-10) o escribe 'salir' para terminar: ")
    
    if entrada.lower() == "salir":
        print("Has decidido salir del juego.")
    elif entrada.isdigit():  # Verificamos que sea un número
        adivinanza = int(entrada)
        if adivinanza == numero_secreto:
            print("¡Correcto! ¡Lo adivinaste!")
            break  # Salimos solo si acierta
        else:
            print("Número incorrecto, intenta otra vez.")
    else:
        print("Entrada inválida. Escribe un número o 'salir'.")
