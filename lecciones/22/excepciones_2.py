def divide():
    try:
        op1 = (float(input("Dividendo: ")))
        op2 = (float(input("Divisor: ")))
        print("La división resulta: " + str(op1 / op2))
    except ValueError:
        print("El valor introducido es erróneo.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    finally:
        print("Cálculo finalizado.")


divide()
