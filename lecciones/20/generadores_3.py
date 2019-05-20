def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento


# Creamos objeto generador
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao",
                                       "Valencia")

print(next(ciudades_devueltas))  # M

print(next(ciudades_devueltas))  # a
