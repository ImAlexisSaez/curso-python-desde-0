email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(arroba)
