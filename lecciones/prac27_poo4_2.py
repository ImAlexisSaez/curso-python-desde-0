class Coche():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False

    def arrancar(self, arrancamos):
        self.en_marcha = arrancamos
        if self.en_marcha:
            return "El coche está en marcha."
        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas. Un ancho de",
              self.ancho_chasis, "cm y un largo de", self.largo_chasis, "cm.")


mi_coche1 = Coche()
mi_coche2 = Coche()

print(mi_coche1.arrancar(True))  # El coche está en marcha.
print(mi_coche2.arrancar(False))  # # El coche está parado.
mi_coche1.estado()
# El coche tiene 4 ruedas. Un ancho de 120 cm y un largo de 250 cm.
mi_coche2.estado()
# El coche tiene 4 ruedas. Un ancho de 120 cm y un largo de 250 cm.
