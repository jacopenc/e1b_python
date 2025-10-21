print("Elige un navegador para realizar tu búsqueda:")
print("1. Google Chrome")
print("2. Mozilla Firefox")
print("3. Microsoft Edge")
print("4. Safari")

opcion = input("Escribe el número de tu elección: ")

match opcion:
    case "1":
        print("Has elegido Google Chrome")
        busqueda = input("Escribe lo que deseas buscar: ")
        print('Buscando "' + busqueda + '" en Google Chrome...')
    case "2":
        print("Has elegido Mozilla Firefox")
        busqueda = input("Escribe lo que deseas buscar: ")
        print('Buscando "' + busqueda + '" en Mozilla Firefox...')
    case "3":
        print("Has elegido Microsoft Edge")
        busqueda = input("Escribe lo que deseas buscar: ")
        print('Buscando "' + busqueda + '" en Microsoft Edge...')
    case "4":
        print("Has elegido Safari")
        busqueda = input("Escribe lo que deseas buscar: ")
        print('Buscando "' + busqueda + '" en Safari...')
    case _:
        print("Navegador no válido")
