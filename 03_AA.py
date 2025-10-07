# Ejemplo con variables y diferentes tipos de datos relacionados con IPs
# con control de cast usando try/except

try:
    ip = input("Indica  dirección IP: ")             
    puerto = int(input("número de puerto: "))   # int
    mascara = input("máscara de red (ej. 255.255.255.0): ") 
    latencia = float(input("latencia en ms: ")) # float
    servidor = input("¿Es un servidor? (sí/no): ")          
except ValueError:
    print("Error: Alguno de los valores numéricos no es válido.")
    puerto = 0
    latencia = 0.0
    ip = "0.0.0.0"
    mascara = "0.0.0.0"
    servidor = "desconocido"

print("\n--- Datos  ---")
print("Dirección IP:", ip)
print("Puerto:", puerto)
print("Máscara de red:", mascara)
print("Latencia:", latencia, "ms")
print("Servidor:", servidor)

