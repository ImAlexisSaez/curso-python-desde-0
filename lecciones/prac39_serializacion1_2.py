import pickle

fichero = open("prac39_files/lista_nombres", "rb")

lista = pickle.load(fichero)

fichero.close()

print(lista)
