import pickle

nombres = ["Pedro", "Ana", "María", "Isabel"]

fichero = open("lista_nombres", "wb")

pickle.dump(nombres, fichero)

fichero.close()

del fichero
