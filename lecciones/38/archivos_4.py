from io import open

archivo = open("archivo2.txt", "r")

archivo.seek(len(archivo.read()) / 2)

print(archivo.read())

archivo.close()
