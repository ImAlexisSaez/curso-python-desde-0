def evalua_edad(edad):
    if edad < 20:
        return "Eres muy joven."
    elif edad < 40:
        return "Eres joven."
    elif edad < 65:
        return "Eres maduro."
    elif edad < 100:
        return "Cuídate."


print(evalua_edad(18))
print(evalua_edad(70))
print(evalua_edad(-15))
