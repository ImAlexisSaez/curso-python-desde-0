from io import open

# Creación + Apertura
archivo_texto = open("archivo.txt", "w")

frase = "Es un estupendo día para estudiar Python\nen Youtube."

# Manipulación
archivo_texto.write(frase)

# Cierre
archivo_texto.close()
