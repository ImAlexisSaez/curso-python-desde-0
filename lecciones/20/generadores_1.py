def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento


# Creamos objeto generador
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao",
                                       "Valencia")

print(next(ciudades_devueltas))  # Madrid

print(next(ciudades_devueltas))  # Barcelona
