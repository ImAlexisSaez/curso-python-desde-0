mi_lista = ["María", "Pepe", "Marta", "Antonio"]

print(mi_lista) # Imprime la lista completa: ["María", "Pepe", "Marta", "Antonio"]
print(mi_lista[:]) # ["María", "Pepe", "Marta", "Antonio"]

print(mi_lista[2]) # Marta
print(mi_lista[0]) # María

print(mi_lista[-1]) # Antonio
print(mi_lista[-3]) # Pepe

print(mi_lista[0:2]) # ["María", "Pepe"]
print(mi_lista[0:1]) # ["María"]
print(mi_lista[-3:-1]) # ["Pepe", "Marta"]

print(mi_lista[:2]) # ["María", "Pepe"]
print(mi_lista[2:]) # ["Marta", "Antonio"]
print(mi_lista[-2:]) # ["Marta", "Antonio"]

print(type(mi_lista[2])) # <class 'str'>
print(type(mi_lista[2:3])) # <class 'list'>

mi_lista.append("Sandra")
print(mi_lista) # ['María', 'Pepe', 'Marta', 'Antonio', 'Sandra']

mi_lista.insert(2, "Paco")
print(mi_lista) # ['María', 'Pepe', 'Paco', 'Marta', 'Antonio', 'Sandra']

mi_compra = ["Manzanas"]
print(mi_compra) # ["Manzanas"]

mi_compra.extend(["Aguacates", "Sandía"])
print(mi_compra) # ["Manzanas", "Aguacates", "Sandía"]

print(mi_lista.index("Antonio")) # 4
print(mi_compra.index("Sandía")) # 2

mi_compra.extend(mi_compra)
print(mi_compra) # ["Manzanas", "Aguacates", "Sandía", "Manzanas", "Aguacates", "Sandía"]
print(mi_compra.index("Manzanas")) # 0

print("Pepe" in mi_lista) # True
print("Ana" in mi_lista) # False

mezcla = ["Alexis", True, 10, 3.14]
print(mezcla) # ["Alexis", True, 10, 3.14]

mezcla.remove(True)
print(mezcla) # ["Alexis", 10, 3.14]

mezcla.pop()
print(mezcla) # ["Alexis", 10]

lista1 = ["Ana", 5]
lista2 = [True, 2.1]
lista3 = lista1 + lista2
print(lista3) # ["Ana", 5, True, 2.1]

print(lista1 * 2) # ["Ana", 5, "Ana", 5]
