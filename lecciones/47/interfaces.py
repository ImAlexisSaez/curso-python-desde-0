from tkinter import Button, Entry, Frame, Tk

# Raíz
raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("icon.ico")

# Frame
frame = Frame(raiz)
frame.pack()

# Pantalla
pantalla = Entry(frame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# Fila 1 de botones
boton7 = Button(frame, text="7", width=3)
boton7.grid(row=2, column=1)
boton8 = Button(frame, text="8", width=3)
boton8.grid(row=2, column=2)
boton9 = Button(frame, text="9", width=3)
boton9.grid(row=2, column=3)
boton_div = Button(frame, text="/", width=3)
boton_div.grid(row=2, column=4)

# Fila 2 de botones
boton4 = Button(frame, text="4", width=3)
boton4.grid(row=3, column=1)
boton5 = Button(frame, text="5", width=3)
boton5.grid(row=3, column=2)
boton6 = Button(frame, text="6", width=3)
boton6.grid(row=3, column=3)
boton_mult = Button(frame, text="*", width=3)
boton_mult.grid(row=3, column=4)

# Fila 3 de botones
boton1 = Button(frame, text="1", width=3)
boton1.grid(row=4, column=1)
boton2 = Button(frame, text="2", width=3)
boton2.grid(row=4, column=2)
boton3 = Button(frame, text="3", width=3)
boton3.grid(row=4, column=3)
boton_rest = Button(frame, text="-", width=3)
boton_rest.grid(row=4, column=4)

# Fila 4 de botones
boton0 = Button(frame, text="0", width=3)
boton0.grid(row=5, column=1)
boton_coma = Button(frame, text=".", width=3)
boton_coma.grid(row=5, column=2)
boton_igual = Button(frame, text="=", width=3)
boton_igual.grid(row=5, column=3)
boton_suma = Button(frame, text="+", width=3)
boton_suma.grid(row=5, column=4)

raiz.mainloop()
