from io import open

archivo = open("prac38_files/archivo2.txt", "r")

print(archivo.read())

archivo.close()
