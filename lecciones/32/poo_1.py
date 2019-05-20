class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas.")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas.")


class Camion():
    def desplazmaiento(self):
        print("Me desplazo utilizando seis ruedas.")


mi_vehiculo = Moto()

mi_vehiculo.desplazamiento()

mi_vehiculo2 = Coche()

mi_vehiculo2.desplazamiento()

mi_vehiculo3 = Camion()

mi_vehiculo3.desplazmaiento()
