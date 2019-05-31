import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("INSERT INTO PRODUCTOS VALUES (NULL, 'Pelota', 57, 'Deportes')")

mi_conexion.commit()

mi_conexion.close()
