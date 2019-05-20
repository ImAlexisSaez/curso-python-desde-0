print("Control de calificaciones")

nota_alumno = int(input("Introduce la nota: "))

if nota_alumno < 0:
    print("Nota incorrecta.")
elif nota_alumno < 5:
    print("Insuficiente.")
elif nota_alumno < 6:
    print("Suficiente.")
elif nota_alumno < 7:
    print("Bien.")
elif nota_alumno < 9:
    print("Notable")
elif nota_alumno <= 10:
    print("Sobresaliente")
else:
    print("Nota incorrecta.")
