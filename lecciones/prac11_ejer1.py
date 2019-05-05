def devuelve_max(n1, n2):
    if n1 < n2:
        return n2
    else:
        return n1


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print("El máximo es: " + str(devuelve_max(num1, num2)))
