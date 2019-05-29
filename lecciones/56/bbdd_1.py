import sqlite3

mi_conexion = sqlite3.connect("base-de-datos")

mi_cursor = mi_conexion.cursor()

productos = [("Camiseta", 10, "Deportes"), ("Jarrón", 90, "Cerámica"),
             ("Camión", 20, "Juguetería")]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", productos)

mi_conexion.commit()

mi_conexion.close()
