# Clase Padre
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:",
              self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:",
              self.frena)


# Clase hija
class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito."

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:",
              self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:",
              self.frena, "\n", self.hcaballito)


mi_moto = Moto("Honda", "CBR")

mi_moto.caballito()

mi_moto.estado()
