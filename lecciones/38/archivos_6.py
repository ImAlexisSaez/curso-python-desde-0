from io import open

archivo = open("archivo3.txt", "r+")  # lectura y escritura

archivo.write("Comienzo del texto: ")

archivo.seek(0)

print(archivo.read())

archivo.close()
