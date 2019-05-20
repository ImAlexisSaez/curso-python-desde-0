from io import open

archivo = open("archivo2.txt", "r")

archivo.seek(len(archivo.readline()))

print(archivo.read())

archivo.close()
