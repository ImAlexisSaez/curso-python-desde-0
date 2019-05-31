import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")

mi_conexion.commit()

mi_conexion.close()
