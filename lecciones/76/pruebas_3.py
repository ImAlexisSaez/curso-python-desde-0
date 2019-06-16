import doctest


def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    >>> area_triangulo(3, 6)
    'El área del triángulo es 9.0'

    """
    return "El área del triángulo es " + str(base * altura / 2.)


doctest.testmod()
