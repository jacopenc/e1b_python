import subprocess

fichero_salida = "salida.txt"

# modo 'w' → crea o sobrescribe
f = open(fichero_salida, "w")
subprocess.run("dir", stdout=f, stderr=subprocess.STDOUT, shell=True)
f.close()

# modo 'a' → añade al final
f = open(fichero_salida, "a")
subprocess.run('echo Este texto se añade al final', stdout=f, stderr=subprocess.STDOUT, shell=True)
f.close()

print("Salida generada y ampliada en", fichero_salida)
