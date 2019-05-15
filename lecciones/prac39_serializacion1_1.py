import pickle

nombres = ["Pedro", "Ana", "María", "Isabel"]

fichero = open("prac39_files/lista_nombres", "wb")

pickle.dump(nombres, fichero)

fichero.close()

del fichero
