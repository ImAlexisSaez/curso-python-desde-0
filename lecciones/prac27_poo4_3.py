class Coche():
    def __init__(self):
        self.largo_chasis = 250
        self.ancho_chasis = 120
        self.ruedas = 4
        self.en_marcha = False

    def arrancar(self, arrancamos):
        self.en_marcha = arrancamos
        if self.en_marcha:
            return "El coche está en marcha."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas. Un ancho de",
              self.ancho_chasis, "cm y un largo de", self.largo_chasis, "cm.")


mi_coche2 = Coche()

print(mi_coche2.arrancar(False))

mi_coche2.ruedas = 5

mi_coche2.estado()
