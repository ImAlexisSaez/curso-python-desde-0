import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID=1")

mi_conexion.commit()

mi_conexion.close()
