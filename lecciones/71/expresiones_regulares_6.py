import re

codigos = ["Ma.1", "Se1", "Ma2", "Ba1", "Ma:3", "Va1", "Va2", "Ma4",
           "MaA", "Ma.5", "MaB", "Ma:C"]

[print(codigo) for codigo in codigos if re.findall("Ma[.:]", codigo)]
