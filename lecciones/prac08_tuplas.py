mi_tupla = ("Alexis", 10, 1, 1995)

print(mi_tupla)  # ("Alexis", 10, 1, 1995)
print(mi_tupla[1])  # 10
print(mi_tupla[-1])  # 1995

mi_lista = list(mi_tupla)
print(mi_lista)  # ["Alexis", 10, 1, 1995]

mi_tupla = tuple(mi_lista)
print(mi_tupla)  # ("Alexis", 10, 1, 1995)

print("Alexis" in mi_tupla)  # True
print(3.14 in mi_tupla)  # False

mi_tupla = ("Alexis", 1, 2, 2, True, 2, "Alexis")

print(mi_tupla.count("Alexis"))  # 2
print(mi_tupla.count(1))  # 2 (True cuenta como 1)
print(mi_tupla.count(2))  # 3

print(len(mi_tupla))  # 7
print(mi_tupla[len(mi_tupla) - 1])  # "Alexis"

mi_tupla = ("Alexis", )

print(type(mi_tupla))  # <class 'tuple'>
print(len(mi_tupla))  # 1

mi_tupla = "Alexis", 3.14, True, 10

print(type(mi_tupla))  # <class 'tuple'>
print(mi_tupla)  # ("Alexis", 3.14, True, 10)

mi_tupla = ("Alexis", 3.14, True, 10)

nombre, pi, alto, mes = mi_tupla

print(nombre)  # Alexis
print(pi)  # 3.14
print(alto)  # True
print(mes)  # 10

print(mi_tupla.index("Alexis"))
