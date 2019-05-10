class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def describir(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:",
              self.residencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado,
                 residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def describir(self):
        super().describir()
        print("Salario:", self.salario, "\nAntigüedad:", self.antiguedad)


juan = Empleado(1500, 15, "Juan", 33, "Italia")

juan.describir()

print(isinstance(juan, Persona))  # True
print(isinstance(juan, Empleado))  # True

marco = Persona("Marco", 51, "Francia")

print(isinstance(marco, Persona))  # True
print(isinstance(marco, Empleado))  # False
