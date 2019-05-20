import pickle


class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        fichero = open("lista_de_personas", "ab+")
        fichero.seek(0)  # Desplazamos cursor al principio

        try:
            self.personas = pickle.load(fichero)  # Cargamos información
            print("Se cargaron {} personas.".format(len(self.personas)))
        except EOFError:
            print("El fichero está vacío.")  # Para la primera vez que abrimos
        finally:
            fichero.close()
            del fichero

    def agregar_personas(self, persona):
        self.personas.append(persona)
        self.guardar_personas()

    def mostrar_personas(self):
        for persona in self.personas:
            print(persona.__str__())

    def guardar_personas(self):
        fichero = open("lista_de_personas", "wb")
        pickle.dump(self.personas, fichero)
        fichero.close()
        del fichero

    def mostrar_informacion(self):
        print("La información del fichero externo es la siguiente:")
        for persona in self.personas:
            print(persona.__str__())


lista_personas = ListaPersonas()

sandra = Persona("Sandra", "Femenino", "29")
lista_personas.agregar_personas(sandra)

antonio = Persona("Antonio", "Masculino", "39")
lista_personas.agregar_personas(antonio)

ana = Persona("Ana", "Femenino", "20")
lista_personas.agregar_personas(ana)

lista_personas.mostrar_informacion()

juan = Persona("Juan", "Masculino", "47")
lista_personas.agregar_personas(juan)

lista_personas.mostrar_informacion()
