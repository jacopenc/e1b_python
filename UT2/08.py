color = "rojo"

match color:
    case "rojo":
        print("Alto")
    case "amarillo":
        print("Precaución")
    case "verde":
        print("Avanza")
    case _:
        print("Color desconocido")
