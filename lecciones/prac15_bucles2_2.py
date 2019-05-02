email = False

for i in "direccion@dominio.com":
	if i == "@":
		email = True

if email == True:
	print("El email es correcto.")
else:
	print("El email no es correcto.")

email = False

for i in "direccion@dominio.com":
	if i == "@":
		email = True

if email:
	print("El email es correcto.")
else:
	print("El email no es correcto.")