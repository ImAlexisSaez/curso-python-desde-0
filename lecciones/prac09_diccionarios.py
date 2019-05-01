mi_dicc = {"Alemania": "Berlin",
           "Francia": "París",
           "Reino Unido": "Londres",
           "España": "Madrid"}

print(mi_dicc["Francia"]) # París
print(mi_dicc["España"]) # Madrid

print(mi_dicc) # {'Alemania': 'Berlin', 'Francia': 'París', 'Reino Unido': 'Londres', 'España': 'Madrid'}

mi_dicc["Italia"] = "Lisboa"

print(mi_dicc)
# {'Alemania': 'Berlin', 'Francia': 'París', 'Reino Unido': 'Londres', 'España': 'Madrid', 'Italia': 'Lisboa'}

mi_dicc["Italia"] = "Roma"

print(mi_dicc)
# {'Alemania': 'Berlin', 'Francia': 'París', 'Reino Unido': 'Londres', 'España': 'Madrid', 'Italia': 'Roma'}

del mi_dicc["Reino Unido"]

print(mi_dicc)
# {'Alemania': 'Berlin', 'Francia': 'París', 'España': 'Madrid', 'Italia': 'Roma'}

mi_dicc = {"Alemania": "Berlín",
           23: "Jordan",
           "Mosqueteros": 3}

print(mi_dicc) # {'Alemania': 'Berlín', 23: 'Jordan', 'Mosqueteros': 3}

mi_tupla = ("España", "Francia", "Reino Unido", "Alemania")
mi_dicc = {mi_tupla[0]: "Madrid",
           mi_tupla[1]: "París",
           mi_tupla[2]: "Londres",
           mi_tupla[3]: "Berlín"}

print(mi_dicc) # {'España': 'Madrid', 'Francia': 'París', 'Reino Unido': 'Londres', 'Alemania': 'Berlín'}

print(mi_dicc["España"]) # Madrid
print(mi_dicc[mi_tupla[0]]) # Madrid

mi_dicc = {23: "Jordan",
           "Nombre": "Michael",
           "Equipo": "Chicago",
           "Anillos": (1991, 1992, 1993, 1996, 1997, 1998)}

print(mi_dicc) # {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'Anillos': (1991, 1992, 1993, 1996, 1997, 1998)}
print(mi_dicc["Equipo"]) # Chicago
print(mi_dicc["Anillos"]) # (1991, 1992, 1993, 1996, 1997, 1998)

mi_dicc = {23: "Jordan",
           "Nombre": "Michael",
           "Equipo": "Chicago",
           "Anillos": {"Temporadas": (1991, 1992, 1993, 1996, 1997, 1998)}}

print(mi_dicc) # {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'Anillos': {'Temporadas': (1991, 1992, 1993, 1996, 1997, 1998)}}
print(mi_dicc["Anillos"]) # {'Temporadas': (1991, 1992, 1993, 1996, 1997, 1998)}

print(mi_dicc.keys()) # dict_keys([23, 'Nombre', 'Equipo', 'Anillos'])
print(mi_dicc.values()) # dict_values(['Jordan', 'Michael', 'Chicago', {'Temporadas': (1991, 1992, 1993, 1996, 1997, 1998)}])
print(len(mi_dicc)) # 4
