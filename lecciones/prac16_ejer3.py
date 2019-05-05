def evalua_mail(mail):
    arroba = False
    punto = False

    if "." in mail:
        punto = True

    contador = 0
    for i in mail:
        if i == "@":
            contador += 1

    if contador == 1:
        arroba = True

    return punto and arroba


mail = input("Introduce dirección de correo electrónico: ")

if evalua_mail(mail):
    print("Dirección de correo electrónico VÁLIDA.")
else:
    print("Dirección de correo electrónico INVÁLIDA.")
