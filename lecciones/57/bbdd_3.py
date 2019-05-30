import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03', 'Portátil', 750, 'Informática')")

mi_conexion.commit()

mi_conexion.close()
