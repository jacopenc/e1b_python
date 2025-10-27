import platform
#Arquitectura del sistema (32 o 64 bits)
arquitectura = platform.architecture()
print("Arquitectura:", arquitectura)
bit =arquitectura[0]
print("bits:", bit)