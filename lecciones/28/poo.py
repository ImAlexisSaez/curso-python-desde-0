class Coche():
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False

    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos

        if self.__en_marcha:
            chequeo = self.__chequeo_interno()

        if self.__en_marcha and chequeo:
            return "El coche está en marcha."
        elif self.__en_marcha and not chequeo:
            return "Algo ha ido mal en el chequeo. No podemos arrancar."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de",
              self.__ancho_chasis, "cm y un largo de", self.__largo_chasis,
              "cm.")

    def __chequeo_interno(self):
        print("Realizando chequeo interno.")

        self.gas = "Ok"
        self.aceite = "Ok"
        self.puertas = "Ok"

        if self.gas == "Ok" and self.aceite == "Ok" and self.puertas == "Ok":
            return True
        else:
            return False


mi_coche1 = Coche()

print(mi_coche1.arrancar(True))

mi_coche1.estado()

print("---- Segundo vehículo ----")

mi_coche2 = Coche()

print(mi_coche2.arrancar(False))

mi_coche2.estado()
