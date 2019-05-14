from io import open

archivo = open("prac38_files/archivo3.txt", "r+")  # lectura y escritura

archivo.write("Comienzo del texto: ")

archivo.seek(0)

print(archivo.read())

archivo.close()
