def evaluacion(nota):
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Suspenso"
	return valoracion

print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ")

print(evaluacion(int(nota_alumno)))
