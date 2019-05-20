def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
        return "Operación errónea."


op1 = (int(input("Introduce el primer número: ")))
op2 = (int(input("Introduce el segundo número: ")))

print("Operaciones disponibles: ")
print("- Suma")
print("- Resta")
print("- Multiplica")
print("- Divide")

operacion = input("Introduce la operación a realizar: ")

if operacion == "Suma":
    print(suma(op1, op2))
elif operacion == "Resta":
    print(resta(op1, op2))
elif operacion == "Multiplica":
    print(multiplica(op1, op2))
elif operacion == "Divide":
    print(divide(op1, op2))
else:
    print("Operación no contemplada.")

print("Operación ejecutada. Continuación de ejecución del programa ")
