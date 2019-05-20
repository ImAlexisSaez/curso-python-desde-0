def genera_pares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


# Creo el objeto iterable que genera la función
devuelve_pares = genera_pares(10)

print(next(devuelve_pares))  # 2

print("Aquí podría ir más código.")

print(next(devuelve_pares))  # 4

print("Aquí podría ir más código.")

print(next(devuelve_pares))  # 6
