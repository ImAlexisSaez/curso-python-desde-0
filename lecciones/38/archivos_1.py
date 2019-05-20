from io import open

archivo = open("archivo2.txt", "r")

print(archivo.read())

archivo.close()
