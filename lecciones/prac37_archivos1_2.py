from io import open

archivo_texto = open("prac37_files/archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)
