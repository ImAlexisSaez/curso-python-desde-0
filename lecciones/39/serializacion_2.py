import pickle

fichero = open("lista_nombres", "rb")

lista = pickle.load(fichero)

fichero.close()

print(lista)
