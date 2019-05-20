from io import open

archivo = open("archivo2.txt", "r")

print(archivo.read())

archivo.seek(0)  # Reinicio posición puntero

print(archivo.read())

archivo.seek(10)  # Establezco posición puntero en carácter 10

print(archivo.read())

archivo.close()
