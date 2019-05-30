import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')

productos = [("AR01", "Pelota", 20, "Juguetería"),
             ("AR02", "Pantalón", 15, "Confección"),
             ("AR03", "Destornillador", 25, "Ferretería"),
             ("AR04", "Jarrón", 45, "Cerámica")]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?, ?)", productos)

mi_conexion.commit()

mi_conexion.close()
