class Coche():
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False

    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos
        if self.__en_marcha:
            return "El coche está en marcha."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de",
              self.__ancho_chasis, "cm y un largo de", self.__largo_chasis,
              "cm.")


mi_coche2 = Coche()

print(mi_coche2.arrancar(False))

mi_coche2.__ruedas = 5

mi_coche2.estado()
