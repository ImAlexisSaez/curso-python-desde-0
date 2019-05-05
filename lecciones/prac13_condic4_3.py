print("Asignaturas optativas - Curso 2018/19")

print("- Informática gráfica")
print("- Pruebas de software")
print("- Usabilidad y accesibilidad")

asignatura = input("Escoge la asignatura optativa: ")

if asignatura in ("Informática gráfica", "Pruebas de software",
                  "Usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no está contemplada.")
