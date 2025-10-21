edad = 20
tiene_identificacion = True

if edad >= 18:
    if tiene_identificacion:
        print("Puedes entrar")
    else:
        print("Necesitas una identificación")
else:
    print("No puedes entrar, eres menor de edad")
