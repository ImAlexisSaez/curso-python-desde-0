import re

urls = ["hombres", "mujeres", "mascotas", "camión", "camion"]

[print(url) for url in urls if re.findall("cami[oó]n", url)]
