from tkinter import Menu, Tk

raiz = Tk()
raiz.title("Menús")
raiz.iconbitmap("icon.ico")

barra_menu = Menu(raiz)

raiz.config(menu=barra_menu, width=300, height=300)

archivo_menu = Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar como...")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar")
archivo_menu.add_command(label="Salir")

edicion_menu = Menu(barra_menu, tearoff=0)
edicion_menu.add_command(label="Copiar")
edicion_menu.add_command(label="Cortar")
edicion_menu.add_command(label="Pegar")

herramientas_menu = Menu(barra_menu, tearoff=0)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Licencia")
ayuda_menu.add_separator()
ayuda_menu.add_command(label="Acerca de...")

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=edicion_menu)
barra_menu.add_cascade(label="Herramientas", menu=herramientas_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

raiz.mainloop()
