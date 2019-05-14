from io import open

archivo = open("prac38_files/archivo3.txt", "r+")  # lectura y escritura

lineas = archivo.readlines()

lineas[1] = "Esta línea ha sido incluida desde el exterior.\n"

archivo.seek(0)

archivo.writelines(lineas)

archivo.seek(0)

print(archivo.read())

archivo.close()
