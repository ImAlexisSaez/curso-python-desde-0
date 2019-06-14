def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")
        funcion_parametro(*args)
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo.")
    return funcion_interior


@funcion_decoradora
def suma(n1, n2):
    print(n1 + n2)


@funcion_decoradora
def resta(n1, n2):
    print(n1 - n2)


suma(10, 5)
resta(25, 20)
