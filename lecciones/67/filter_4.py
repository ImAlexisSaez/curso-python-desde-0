class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} y cobra {self.salario} €."


lista_empleados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidenta", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000)
]

salarios_altos = filter(lambda e: e.salario > 50000, lista_empleados)

[print(s.__str__()) for s in salarios_altos]
