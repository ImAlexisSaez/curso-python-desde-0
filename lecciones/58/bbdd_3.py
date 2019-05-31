import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")

productos = mi_cursor.fetchall()

for producto in productos:
    print(producto)

mi_conexion.commit()

mi_conexion.close()
