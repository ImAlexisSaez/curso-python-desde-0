from tkinter import IntVar, Label, Radiobutton, Tk

raiz = Tk()
raiz.title("Botones de radio")
raiz.iconbitmap("icon.ico")

opcion = IntVar()


def imprimir():
    print(opcion.get())


Label(raiz, text="Género:").pack()
Radiobutton(raiz, text="Femenino", variable=opcion, value=1,
            command=imprimir).pack()
Radiobutton(raiz, text="Masculino", variable=opcion, value=2,
            command=imprimir).pack()

raiz.mainloop()
