def comprueba_edad(edad):
    if 0 < edad < 100:
        print("La edad es correcta.")
    else:
        print("La edad es incorrecta.")


comprueba_edad(5)  # La edad es correcta.
comprueba_edad(135)  # La edad es incorrecta.
comprueba_edad(-7)  # La edad es incorrecta.
