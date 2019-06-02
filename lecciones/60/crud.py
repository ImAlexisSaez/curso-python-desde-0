from tkinter import Entry, Frame, Label, Menu, messagebox, Scrollbar, Text, Tk
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

id_entry = Entry(campos_frame)
id_entry.grid(row=0, column=1, padx=2, pady=2)

name_entry = Entry(campos_frame)
name_entry.grid(row=1, column=1, padx=2, pady=2)

lastname_entry = Entry(campos_frame)
lastname_entry.grid(row=2, column=1, padx=2, pady=2)

address_entry = Entry(campos_frame)
address_entry.grid(row=3, column=1, padx=2, pady=2)

password_entry = Entry(campos_frame)
password_entry.grid(row=4, column=1, padx=2, pady=2)
password_entry.config(show="*")

comment_text = Text(campos_frame, width=15, height=5)
comment_text.grid(row=5, column=1, padx=2, pady=2)
comment_text_scrollvert = Scrollbar(campos_frame, command=comment_text.yview)
comment_text_scrollvert.grid(row=5, column=2, sticky="nsew")
comment_text.config(yscrollcommand=comment_text_scrollvert)

# Frame inferior

# Ejecución de la aplicación
root.mainloop()
