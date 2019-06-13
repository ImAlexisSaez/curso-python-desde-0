import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"

if re.match("Sandra", nombre1):
    print("Hemos encontrado el nombre.")
else:
    print("No hemos encontrado el nombre.")
