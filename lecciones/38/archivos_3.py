from io import open

archivo = open("archivo2.txt", "r")

print(archivo.read(11))
print(archivo.read())

archivo.close()
