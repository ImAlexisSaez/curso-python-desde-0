class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def describir(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:",
              self.residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        self.salario = salario
        self.antiguedad = antiguedad


antonio = Persona("Antonio", 55, "España")

antonio.describir()

juan = Empleado(1500, 15)

juan.describir()
