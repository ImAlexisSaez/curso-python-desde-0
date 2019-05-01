print("Asignaturas optativas - Curso 2018/19")

print("- Informática gráfica")
print("- Pruebas de software")
print("- Usabilidad y accesibilidad")

opcion = input("Escoge la asignatura optativa: ")

asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no está contemplada.")
