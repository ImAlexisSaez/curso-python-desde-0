edad = int(input("Introduce tu edad: "))

while edad < 0 or edad > 110:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo.")
    edad = int(input("Introduce tu edad: "))

print(f"Tienes {edad} años. Gracias por colaborar.")
