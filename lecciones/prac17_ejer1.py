numero = int(input("Introduce un número entero: "))

condicion = True

while condicion:
	num1 = numero
	numero = int(input("Introduce un número entero mayor que el anterior: "))
	if num1 > numero:
		print(f"Valor incorrecto: {num1} no es mayor que {numero}.")
		condicion = False
	else:
		print(f"Valor correcto: {numero} es mayor que {num1}")
