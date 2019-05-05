def genera_pares(limite):
    num = 1
    lista_pares = []
    while num < limite:
        lista_pares.append(num * 2)
        num += 1
    return lista_pares


print(genera_pares(10))  # [2, 4, 6, 8, 10, 12, 14, 16, 18]
