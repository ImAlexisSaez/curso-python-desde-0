def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado su lado."""
    return "El área del cuadrado es: " + str(lado * lado)


def area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y su altura."""
    return "El área del triángulo es: " + str(base * altura / 2.)


# print(area_cuadrado(5))
# print(area_triangulo(3, 6))

# print(area_cuadrado.__doc__)
# print(area_triangulo.__doc__)

help(area_cuadrado)
help(area_triangulo)
