def evalua_email(direcc):
    email = False

    for i in direcc:
        if i == "@":
            email = True
    if email:
        print("El email es correcto.")
    else:
        print("El email no es correcto.")


direcc = input("Introduce tu dirección de correo electrónico: ")

evalua_email(direcc)
