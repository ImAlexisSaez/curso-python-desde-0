from tkinter import Button, Entry, Frame, Label, Menu, messagebox, Scrollbar, Text, Tk
import sqlite3

# Raíz de la aplicación
root = Tk()
root.title("Aplicación CRUD")
root.iconbitmap("icon.ico")

# Menú superior de la aplicación
barra_menu = Menu(root)
root.config(menu=barra_menu)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar")
bbdd_menu.add_separator()
bbdd_menu.add_command(label="Salir")

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos")

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
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

id_label = Label(campos_frame, text="ID:")
id_label.grid(row=0, column=0, sticky="e", padx=2, pady=2)

id_entry = Entry(campos_frame, width=40)
id_entry.grid(row=0, column=1, padx=2, pady=2)

name_label = Label(campos_frame, text="Nombre:")
name_label.grid(row=1, column=0, sticky="e", padx=2, pady=2)

name_entry = Entry(campos_frame, width=40)
name_entry.grid(row=1, column=1, padx=2, pady=2)

lastname_label = Label(campos_frame, text="Apellido:")
lastname_label.grid(row=2, column=0, sticky="e", padx=2, pady=2)

lastname_entry = Entry(campos_frame, width=40)
lastname_entry.grid(row=2, column=1, padx=2, pady=2)

address_label = Label(campos_frame, text="Dirección:")
address_label.grid(row=3, column=0, sticky="e", padx=2, pady=2)

address_entry = Entry(campos_frame, width=40)
address_entry.grid(row=3, column=1, padx=2, pady=2)

password_label = Label(campos_frame, text="Contraseña:")
password_label.grid(row=4, column=0, sticky="e", padx=2, pady=2)

password_entry = Entry(campos_frame, width=40)
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

crear_button = Button(botones_frame, text="Create")
crear_button.grid(row=0, column=0, sticky="e", padx=2, pady=2)

read_button = Button(botones_frame, text="Read")
read_button.grid(row=0, column=1, sticky="e", padx=2, pady=2)

update_button = Button(botones_frame, text="Update")
update_button.grid(row=0, column=2, sticky="e", padx=2, pady=2)

delete_button = Button(botones_frame, text="Delete")
delete_button.grid(row=0, column=3, sticky="e", padx=2, pady=2)

# Ejecución de la aplicación
root.mainloop()
