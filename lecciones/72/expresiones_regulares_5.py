import re

nombres = ["Sandra López", "Antonio Gómez", "María López",
           "Jara Martín", "Lara Pérez"]

[print(nombre, end="\n") for nombre in nombres if re.search("López", nombre)]
