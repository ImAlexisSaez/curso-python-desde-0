from io import open

archivo1 = open("prac37_files/archivo.txt", "r")
texto = archivo1.read()
archivo1.close()

archivo2 = open("prac37_files/archivo2.txt", "w")
archivo2.write(texto)
archivo2.close()

archivo2 = open("prac37_files/archivo2.txt", "a")
archivo2.write("\n¡Mañana más!")
archivo2.close()
