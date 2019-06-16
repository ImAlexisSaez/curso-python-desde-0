import doctest


def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    >>> area_triangulo(3, 6)
    8.0

    """
    return base * altura / 2.


doctest.testmod()
