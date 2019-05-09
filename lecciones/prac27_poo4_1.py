class Coche():
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False

    def arrancar(self):
        self.en_marcha = True

    def estado(self):
        if self.en_marcha:
            return "El coche está en marcha."
        else:
            return "El coche está parado."


mi_coche1 = Coche()
mi_coche2 = Coche()

print("Largo mi_coche1: ", mi_coche1.largo_chasis)  # Largo mi_coche1:  250
print("Largo mi_coche2: ", mi_coche2.largo_chasis)  # Largo mi_coche2:  250

mi_coche1.arrancar()
print(mi_coche1.estado())  # El coche está en marcha.
print(mi_coche2.estado())  # El coche está parado.
