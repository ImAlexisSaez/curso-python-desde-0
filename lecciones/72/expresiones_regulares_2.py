import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "Jara Martín"
nombre5 = "Lara Pérez"

if re.match("sandra", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre.")
else:
    print("No hemos encontrado el nombre.")
