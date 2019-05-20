nombre = "Píldoras Informáticas"

print(len(nombre))  # 21 (considera espacio en blanco como carácter)

contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print(contador)  # 20
