import re

cadena = "Vamos a aprender expresiones regulares."

texto_buscar = "aprender"

if re.search(texto_buscar, cadena) is not None:
    print("Texto encontrado.")
else:
    print("Texto no encontrado.")
