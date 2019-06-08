def numero_par(num):
    return num % 2 == 0


numeros = [17, 24, 7, 39, 8, 51, 92]

print(filter(numero_par, numeros))  # objeto iterable

print(list(filter(numero_par, numeros)))
