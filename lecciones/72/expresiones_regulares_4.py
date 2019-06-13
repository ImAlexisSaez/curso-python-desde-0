import re

datos = ["Alexis Sáez", "123456789", "Number1"]

[print(d) for d in datos if re.match("\d", d)]
