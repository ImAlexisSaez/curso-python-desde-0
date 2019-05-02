def evalua_password(password):
	valido = True
	if len(password) < 8 or " " in password:
		valido = False
	return valido

password = input("Introduce contraseña: ")

if evalua_password(password):
	print("Constraseña OK.")
else:
	print("Contraseña errónea.")
