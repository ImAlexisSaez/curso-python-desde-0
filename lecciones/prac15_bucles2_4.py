def evalua_email(direcc):
    arroba = False
    punto = False

    for i in direcc:
        if i == "@":
            arroba = True
        if i == ".":
            punto = True
    if arroba and punto:
        print("El email es correcto.")
    else:
        print("El email no es correcto.")

direcc = input("Introduce tu dirección de correo electrónico: ")

evalua_email(direcc)