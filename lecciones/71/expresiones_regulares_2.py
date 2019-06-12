import re

nombres = ["Ana", "Pedro", "María", "Rosa", "Sandra", "Celia"]

[print(nombre) for nombre in nombres if re.findall("^[o-t]", nombre)]
