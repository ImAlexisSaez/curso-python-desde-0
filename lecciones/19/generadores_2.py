def genera_pares(limite):
    num = 1
    while num < limite:
        yield num * 2
        num += 1


# Creo el objeto iterable que genera la función
devuelve_pares = genera_pares(10)

# Recorro el objeto iterable con, por ejemplo, un bucle for
for i in devuelve_pares:
    print(i)

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
