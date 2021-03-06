from tkinter import Button, END, Entry, Frame, Label, Menu, messagebox, Scrollbar, StringVar, Text, Tk
import sqlite3


# Función para conectar a la BBDD
def conecta_bbdd():
    conexion = sqlite3.connect("usuarios")
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            PASSWORD VARCHAR(50),
            COMENTARIOS VARCHAR(250))
            ''')
    except sqlite3.OperationalError:
        pass
    finally:
        messagebox.showinfo(
            title="Conexión a la base de datos",
            message="La conexión a la base de datos se ha realizado con éxito."
        )


# Función para salir de la aplicación
def sale_aplicacion():
    valor = messagebox.askquestion(
        title="Salir", message="¿Deseas realmente salir de la aplicación?")
    if valor == "yes":
        root.destroy()


# Función que limpia los registros de la aplicación
def limpia_registros():
    id_data.set("")
    name_data.set("")
    lastname_data.set("")
    address_data.set("")
    password_data.set("")
    comment_text.delete(1.0, END)


# Función que inserta registros en la BBDD
def crud_create():
    conexion = sqlite3.connect("usuarios")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO DATOS_USUARIOS VALUES (NULL, '" +
                   name_data.get() + "', '" + lastname_data.get() + "','" +
                   address_data.get() + "','" + password_data.get() + "','" +
                   comment_text.get("1.0", END) + "')")
    conexion.commit()
    messagebox.showinfo(
        title="Crear registro",
        message="Registro insertado con éxito en la base de datos.")
    conexion.close()


# Función que lee registros de la BBDD
def crud_read():
    conexion = sqlite3.connect("usuarios")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + id_data.get())
    usuario = cursor.fetchall()
    for u in usuario:
        id_data.set(u[0])
        name_data.set(u[1])
        lastname_data.set(u[2])
        address_data.set(u[3])
        password_data.set(u[4])
        comment_text.insert(1.0, u[5])
    conexion.commit()
    conexion.close()


# Función que actualiza registros de la BBDD
def crud_update():
    conexion = sqlite3.connect("usuarios")
    cursor = conexion.cursor()
    cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='" +
                   name_data.get() + "', APELLIDO='" + lastname_data.get() +
                   "', DIRECCION='" + address_data.get() + "', PASSWORD='" +
                   password_data.get() + "', COMENTARIOS='" +
                   comment_text.get("1.0", END) + "'")
    conexion.commit()
    messagebox.showinfo(
        title="Actualizar registro",
        message="Registro actualizado con éxito en la base de datos.")
    conexion.close()


# Raíz de la aplicación
root = Tk()
root.title("Aplicación CRUD")
root.iconbitmap("icon.ico")

# Menú superior de la aplicación
barra_menu = Menu(root)
root.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conecta_bbdd)
bbdd_menu.add_separator()
bbdd_menu.add_command(label="Salir", command=sale_aplicacion)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos", command=limpia_registros)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crud_create)
crud_menu.add_command(label="Leer", command=crud_read)
crud_menu.add_command(label="Actualizar", command=crud_update)
crud_menu.add_command(label="Borrar")

help_menu = Menu(barra_menu, tearoff=0)
help_menu.add_command(label="Licencia")
help_menu.add_separator()
help_menu.add_command(label="Acerca de...")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=help_menu)

# Frame superior
campos_frame = Frame(root)
campos_frame.pack()

id_data = StringVar()
name_data = StringVar()
lastname_data = StringVar()
address_data = StringVar()
password_data = StringVar()

id_label = Label(campos_frame, text="ID:")
id_label.grid(row=0, column=0, sticky="e", padx=2, pady=2)

id_entry = Entry(campos_frame, width=40, textvariable=id_data)
id_entry.grid(row=0, column=1, padx=2, pady=2)

name_label = Label(campos_frame, text="Nombre:")
name_label.grid(row=1, column=0, sticky="e", padx=2, pady=2)

name_entry = Entry(campos_frame, width=40, textvariable=name_data)
name_entry.grid(row=1, column=1, padx=2, pady=2)

lastname_label = Label(campos_frame, text="Apellido:")
lastname_label.grid(row=2, column=0, sticky="e", padx=2, pady=2)

lastname_entry = Entry(campos_frame, width=40, textvariable=lastname_data)
lastname_entry.grid(row=2, column=1, padx=2, pady=2)

address_label = Label(campos_frame, text="Dirección:")
address_label.grid(row=3, column=0, sticky="e", padx=2, pady=2)

address_entry = Entry(campos_frame, width=40, textvariable=address_data)
address_entry.grid(row=3, column=1, padx=2, pady=2)

password_label = Label(campos_frame, text="Contraseña:")
password_label.grid(row=4, column=0, sticky="e", padx=2, pady=2)

password_entry = Entry(campos_frame, width=40, textvariable=password_data)
password_entry.grid(row=4, column=1, padx=2, pady=2)
password_entry.config(show="*")

comment_label = Label(campos_frame, text="Comentarios:")
comment_label.grid(row=5, column=0, sticky="ne", padx=2, pady=2)

comment_text = Text(campos_frame, width=30, height=5)
comment_text.grid(row=5, column=1, padx=2, pady=2)
comment_text_scrollvert = Scrollbar(campos_frame, command=comment_text.yview)
comment_text_scrollvert.grid(row=5, column=2, sticky="nsew")
comment_text.config(yscrollcommand=comment_text_scrollvert)

# Frame inferior
botones_frame = Frame(root)
botones_frame.pack(expand=True)

crear_button = Button(botones_frame, text="Create", command=crud_create)
crear_button.grid(row=0, column=0, sticky="e", padx=2, pady=2)

read_button = Button(botones_frame, text="Read", command=crud_read)
read_button.grid(row=0, column=1, sticky="e", padx=2, pady=2)

update_button = Button(botones_frame, text="Update", command=crud_update)
update_button.grid(row=0, column=2, sticky="e", padx=2, pady=2)

delete_button = Button(botones_frame, text="Delete")
delete_button.grid(row=0, column=3, sticky="e", padx=2, pady=2)

# Ejecución de la aplicación
root.mainloop()
