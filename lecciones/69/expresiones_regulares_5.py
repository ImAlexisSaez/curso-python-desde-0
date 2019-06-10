import re

cadena = '''
    Vamos a aprender expresiones regulares en Python.
    Python es un lenguaje de sintaxis sencilla.'''

texto_buscar = "Python"

print(len(re.findall(texto_buscar, cadena)))
