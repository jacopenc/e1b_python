# Ejemplo con variables y diferentes tipos de datos relacionados con red WiFi
# usando try/except para controlar conversiones

try:
    ssid = input("nombre de la red WiFi (SSID): ")    # str
    ancho_banda = float(input("Introduce el ancho de banda en MHz: "))    # float
    seguridad = input("Tipo de seguridad (WPA2/WPA3/abierta): ")   # str
    conectado = input("¿Estás conectado a esta red? (sí/no): ")    # str
except ValueError:
    print("Error: Alguno de los valores numéricos no es válido.")
    ssid = "desconocido"
    ancho_banda = 0.0
    seguridad = "indefinida"
    conectado = "no"

print("\n--- Datos  ---")
print("SSID:", ssid)
print("Ancho de banda:", ancho_banda, "MHz")
print("Seguridad:", seguridad)
print("Conectado:", conectado)
