from tkinter import IntVar, Label, Radiobutton, Tk

raiz = Tk()
raiz.title("Botones de radio")
raiz.iconbitmap("icon.ico")

opcion = IntVar()


def imprimir():
    if opcion.get() == 1:
        etiqueta.config(text="Has elegido género femenino.")
    elif opcion.get() == 2:
        etiqueta.config(text="Has elegido género masculino.")
    else:
        etiqueta.config(text="Has elegido otras opciones para género.")


Label(raiz, text="Género:").pack()
Radiobutton(raiz, text="Femenino", variable=opcion, value=1,
            command=imprimir).pack()
Radiobutton(raiz, text="Masculino", variable=opcion, value=2,
            command=imprimir).pack()
Radiobutton(raiz, text="Otras opciones", variable=opcion, value=3,
            command=imprimir).pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()
