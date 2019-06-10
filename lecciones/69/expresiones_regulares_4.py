import re

cadena = "Vamos a aprender expresiones regulares."

texto_buscar = "aprender"

texto_encontrado = re.search(texto_buscar, cadena)

print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())
