import sqlite3

mi_conexion = sqlite3.connect("gestion-productos")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')

productos = [("Pelota", 20, "Juguetería"),
             ("Pantalón", 15, "Confección"),
             ("Destornillador", 25, "Ferretería"),
             ("Jarrón", 45, "Cerámica")]

mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)",
                      productos)

mi_conexion.commit()

mi_conexion.close()
