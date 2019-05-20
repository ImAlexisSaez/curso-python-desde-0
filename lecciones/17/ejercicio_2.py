print("Cálculo de la suma de una serie de números positivos.")
print("Instrucciones: ")
print("- Introduce tantos números positivos como desees sumar.")
print("- Introduce un número negativo para calcular la suma.")

suma = 0
num = int(input("Introduce un número positivo: "))

while num > 0:
    suma += num
    num = int(input("Introduce un número positivo: "))

print(f"La suma de los valores positivos introducios es {suma}.")
