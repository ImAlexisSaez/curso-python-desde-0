import math


def calcula_raiz(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo.")
    else:
        return math.sqrt(num)


op = (int(input("Introduce un número mayor o igual que cero: ")))

print(calcula_raiz(op))

print("Programa terminado.")
