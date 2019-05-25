from tkinter import IntVar, Radiobutton, Tk

raiz = Tk()
raiz.title("Botones de radio")
raiz.iconbitmap("icon.ico")

opcion = IntVar()

Radiobutton(raiz, text="Femenino", variable=opcion, value=1).pack()
Radiobutton(raiz, text="Masculino", variable=opcion, value=2).pack()

raiz.mainloop()
