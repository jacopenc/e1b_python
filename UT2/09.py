dia = "sábado"

match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Es un día laboral")
    case "sábado" | "domingo":
        print("Es fin de semana")
    case _:
        print("Día no válido")
