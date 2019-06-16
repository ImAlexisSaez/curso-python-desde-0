import doctest


def check_mail(mail_user):
    """
    Evalúa un mail recibido en busca de @.
    Si tiene una @ es correcto.
    Si tiene más de una @ es incorrecto.
    Si la @ está al final es incorrecto.

    >>> check_mail("alexis@cursos.es")
    True

    >>> check_mail("alexiscursos.es@")
    False

    >>> check_mail("alexis.cursos.es")
    False

    >>> check_mail("alexis@cursos@es")
    False
    """

    arroba = mail_user.count("@")
    return not (arroba != 1 or mail_user.rfind('@') == len(mail_user) - 1)


doctest.testmod()
