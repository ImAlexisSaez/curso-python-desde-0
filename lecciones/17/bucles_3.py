import math

print("Programa de cálculo de raíces cuadradas")

numero = int(input("Introduce un número: "))

intentos = 0  # Para ejecutar el bucle while un número de veces determinado

while numero < 0:
    print("No se puede hallar la raíz de un número negativo.")
    if intentos == 2:
        print("Has consumido demasiados intentos.")
        print("El programa ha finalizado")
        break
    numero = int(input("Introduce un número: "))
    if numero < 0:
        intentos += 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}.")
