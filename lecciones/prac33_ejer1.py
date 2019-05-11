email = input("Introduce email: ")

if email.count("@") == 1 and email.count("@", 1, len(email) - 1) == 1:
    print("La dirección de correo es correcta.")
else:
    print("La dirección de correo es incorrecta.")
