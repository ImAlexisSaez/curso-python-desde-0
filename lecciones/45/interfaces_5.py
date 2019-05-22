from tkinter import Tk, Frame, Entry, Label

root = Tk()

root.title("Probando el widget Entry")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

frame = Frame(root, width=450, height=300)
frame.pack()

nombre_label = Label(frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="e", padx=2, pady=2)

cuadro_nombre = Entry(frame)
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
movil_label.grid(row=4, column=0, sticky="e")

movil_texto = Entry(frame)
movil_texto.grid(row=4, column=1)

root.mainloop()
