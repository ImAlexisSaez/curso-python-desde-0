import re

codigos = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4"]

[print(codigo) for codigo in codigos if re.findall("Ma[0-3]", codigo)]
