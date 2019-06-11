import re

lista_nombres = ["Ana Gómez",
                 "María Martín",
                 "Sandra López",
                 "Santiago Martín"]

for nombre in lista_nombres:
    if re.findall("^Sandra", nombre):
        print(nombre)

[print(nombre) for nombre in lista_nombres if re.findall("^Sandra", nombre)]
