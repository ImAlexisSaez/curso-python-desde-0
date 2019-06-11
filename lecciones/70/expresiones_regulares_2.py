import re

lista_nombres = ["Ana Gómez",
                 "María Martín",
                 "Sandra López",
                 "Santiago Martín"]

[print(nombre) for nombre in lista_nombres if re.findall("^S", nombre)]
