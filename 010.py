import subprocess
#SABER USUARIO ACTUAL
# Paso 1: Definir el comando a ejecutar (whoami)
comando = ["whoami"]

# Paso 2: Configurar si queremos la salida como texto
usar_texto = True  # Equivale a text=True

# Paso 3: Configurar si queremos capturar la salida
capturar_salida = subprocess.PIPE  # stdout=subprocess.PIPE

# Paso 4: Ejecutar el comando con subprocess.run()
proceso = subprocess.run(comando, text=usar_texto, stdout=capturar_salida)

# Paso 5: Obtener la salida del comando
salida = proceso.stdout

# Paso 6: Mostrar la salida en pantalla
print("Usuario actual del sistema:\n")
print(salida)
