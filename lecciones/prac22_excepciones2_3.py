def divide():
    try:
        op1 = (float(input("Dividendo: ")))
        op2 = (float(input("Divisor: ")))
        print("La división resulta: " + str(op1 / op2))
    finally:
        print("Cálculo finalizado.")


divide()
