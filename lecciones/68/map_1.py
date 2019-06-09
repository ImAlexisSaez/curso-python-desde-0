class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} trabaja como {self.cargo} y cobra {self.salario} €."


lista_empleados = [
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "Presidenta", 7500),
    Empleado("Antonio", "Administrativo", 1200),
    Empleado("Sara", "Secretaria", 1250),
    Empleado("Mario", "Botones", 1000)
]


def calcula_comision(empleado):
    empleado.salario *= 1.03
    return empleado


lista_empleados_comision = map(calcula_comision, lista_empleados)

[print(e) for e in lista_empleados_comision]
