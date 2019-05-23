from tkinter import Tk, Frame, Button, Entry, Label, Scrollbar, StringVar, Text


def codigo_boton():
    mi_nombre.set("Alexis")


root = Tk()

mi_nombre = StringVar()

root.title("Probando los widgets Text y Button")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

frame = Frame(root, width=450, height=300)
frame.pack()

nombre_label = Label(frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="e", padx=2, pady=2)

cuadro_nombre = Entry(frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=0, column=1, padx=2, pady=2)

apellido_label = Label(frame, text="Apellido:")
apellido_label.grid(row=1, column=0, sticky="e", padx=2, pady=2)

apellido_texto = Entry(frame)
apellido_texto.grid(row=1, column=1, padx=2, pady=2)

direccion_label = Label(frame, text="Dirección:")
direccion_label.grid(row=2, column=0, sticky="e", padx=2, pady=2)

direccion_texto = Entry(frame)
direccion_texto.grid(row=2, column=1, padx=2, pady=2)

tfno_label = Label(frame, text="Teléfono (fijo):")
tfno_label.grid(row=3, column=0, sticky="e", padx=2, pady=2)

tfno_texto = Entry(frame)
tfno_texto.grid(row=3, column=1, padx=2, pady=2)

movil_label = Label(frame, text="Teléfono (móvil):")
movil_label.grid(row=4, column=0, sticky="e", padx=2, pady=2)

movil_texto = Entry(frame)
movil_texto.grid(row=4, column=1, padx=2, pady=2)

pass_label = Label(frame, text="Constraseña:")
pass_label.grid(row=5, column=0, sticky="e", padx=2, pady=2)

pass_texto = Entry(frame)
pass_texto.grid(row=5, column=1, padx=2, pady=2)
pass_texto.config(show="*")

bio_label = Label(frame, text="Biografía:")
bio_label.grid(row=6, column=0, sticky="e", padx=2, pady=2)

bio_texto = Text(frame, width=15, height=5)
bio_texto.grid(row=6, column=1, padx=2, pady=2)

scroll_vert = Scrollbar(frame, command=bio_texto.yview)
scroll_vert.grid(row=6, column=2, sticky="nsew")
bio_texto.config(yscrollcommand=scroll_vert.set)

boton_envio = Button(root, text="Enviar", command=codigo_boton)
boton_envio.pack()

root.mainloop()
