import sqlite3

mi_conexion = sqlite3.connect("base-de-datos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("SELECT * FROM PRODUCTOS")

productos = mi_cursor.fetchall()

print(productos)

mi_conexion.close()
