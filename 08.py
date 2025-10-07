import subprocess

# Paso 1: Definir el host y la cantidad de pings
host = "google.com"
cantidad = "4"

# Paso 2: Crear el comando como lista
comando = ["ping", "-n", cantidad, host]

# Paso 3: Configurar los argumentos de subprocess.run()
usar_texto = True  # Equivale a text=True
capturar_salida = subprocess.PIPE  # Equivale a stdout=subprocess.PIPE

# Paso 4: Ejecutar el comando usando las variables
proceso = subprocess.run(comando, text=usar_texto, stdout=capturar_salida)

# Paso 5: Obtener la salida del ping
salida = proceso.stdout

# Paso 6: Mostrar el resultado
print("Resultado del ping:\n")
print(salida)
