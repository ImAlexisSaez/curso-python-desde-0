import doctest
import math


def raiz_cuadrada(lista_numeros):
    """
    La función devuelve una lista con la raíz cuadrada de
    los elementos numéricos pasados por parámetros en otra
    lista.

    >>> lista = []
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raiz_cuadrada(lista)
    [2.0, 3.0, 4.0]
    """
    return [math.sqrt(n) for n in lista_numeros]


doctest.testmod()
