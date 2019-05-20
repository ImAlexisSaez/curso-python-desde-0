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


mi_coche = Coche()  # Instanciación de una clase

print("Largo del coche: ", mi_coche.largo_chasis)  # Largo del coche:  250
print("Número de ruedas: ", mi_coche.ruedas)  # Número de ruedas:  4

# print("En marcha: ", mi_coche.en_marcha)  # En marcha:  False
# mi_coche.arrancar()
# print("En marcha: ", mi_coche.en_marcha)  # En marcha:  True

print(mi_coche.estado())  # El coche está parado.
mi_coche.arrancar()
print(mi_coche.estado())  # El coche está en marcha.
