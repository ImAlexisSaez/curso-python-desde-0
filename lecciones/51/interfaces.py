from tkinter import Checkbutton, Frame, IntVar, Label, PhotoImage, Tk

raiz = Tk()
raiz.title("Casillas de verificación")
raiz.iconbitmap("icon.ico")

playa = IntVar()
montana = IntVar()
turismo_rural = IntVar()


def opciones_viaje():
    opcion_escogida = ""
    if playa.get() == 1:
        opcion_escogida += " playa"
    if montana.get() == 1:
        opcion_escogida += " montaña"
    if turismo_rural.get() == 1:
        opcion_escogida += " turismo rural"
    texto_final.config(text=opcion_escogida)


foto = PhotoImage(file="helicoptero.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Escoge destinos:", width=50).pack()

Checkbutton(frame,
            text="Playa",
            variable=playa,
            onvalue=1,
            offvalue=0,
            command=opciones_viaje).pack()
Checkbutton(frame,
            text="Montaña",
            variable=montana,
            onvalue=1,
            offvalue=0,
            command=opciones_viaje).pack()
Checkbutton(frame,
            text="Turismo rural",
            variable=turismo_rural,
            onvalue=1,
            offvalue=0,
            command=opciones_viaje).pack()

texto_final = Label(frame)
texto_final.pack()

raiz.mainloop()
