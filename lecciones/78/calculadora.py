from tkinter import Button, Entry, Frame, StringVar, Tk

# Raíz
raiz = Tk()
raiz.title("Calculadora")

# Frame
frame = Frame(raiz)
frame.pack()

# Variables
numero_pantalla = StringVar()
operacion = ""
resultado = 0
reset_pantalla = False

# Pantalla
pantalla = Entry(frame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# Pulsaciones teclado
def numero_pulsado(num):
    global operacion, reset_pantalla
    if reset_pantalla:
        numero_pantalla.set(num)
        reset_pantalla = False
    else:
        numero_pantalla.set(numero_pantalla.get() + num)


# Función suma
def suma(num):
    global operacion, reset_pantalla, resultado
    operacion = "suma"
    resultado += int(num)
    reset_pantalla = True
    numero_pantalla.set(resultado)


# Función resta
num1 = 0
contador_resta = 0


def resta(num):
    global contador_resta, num1, operacion, reset_pantalla, resultado
    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()
    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True


# Función multiplicación
contador_multi = 0


def multiplica(num):
    global contador_multi, num1, operacion, reset_pantalla, resultado
    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()
    contador_multi = contador_multi + 1
    operacion = "multiplicacion"
    reset_pantalla = True


# Función división
contador_divi = 0


def divide(num):
    global contador_divi, num1, operacion, reset_pantalla, resultado
    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)
        numero_pantalla.set(resultado)
        resultado = numero_pantalla.get()
    contador_divi = contador_divi + 1
    operacion = "division"
    reset_pantalla = True


# Función el_resultado (para el botón igual)
def el_resultado():
    global contador_divi, contador_multi, contador_resta, operacion, resultado
    if operacion == "suma":
        numero_pantalla.set(resultado + int(numero_pantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numero_pantalla.set(int(resultado) - int(numero_pantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numero_pantalla.set(int(resultado) * int(numero_pantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numero_pantalla.set(int(resultado) / int(numero_pantalla.get()))
        resultado = 0
        contador_divi = 0


# Fila 1 de botones
boton7 = Button(frame, text="7", width=3, command=lambda: numero_pulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text="8", width=3, command=lambda: numero_pulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text="9", width=3, command=lambda: numero_pulsado("9"))
boton9.grid(row=2, column=3)
boton_div = Button(frame,
                   text="/",
                   width=3,
                   command=lambda: divide(numero_pantalla.get()))
boton_div.grid(row=2, column=4)

# Fila 2 de botones
boton4 = Button(frame, text="4", width=3, command=lambda: numero_pulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text="5", width=3, command=lambda: numero_pulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text="6", width=3, command=lambda: numero_pulsado("6"))
boton6.grid(row=3, column=3)
boton_mult = Button(frame,
                    text="*",
                    width=3,
                    command=lambda: multiplica(numero_pantalla.get()))
boton_mult.grid(row=3, column=4)

# Fila 3 de botones
boton1 = Button(frame, text="1", width=3, command=lambda: numero_pulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text="2", width=3, command=lambda: numero_pulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text="3", width=3, command=lambda: numero_pulsado("3"))
boton3.grid(row=4, column=3)
boton_rest = Button(frame,
                    text="-",
                    width=3,
                    command=lambda: resta(numero_pantalla.get()))
boton_rest.grid(row=4, column=4)

# Fila 4 de botones
boton0 = Button(frame, text="0", width=3, command=lambda: numero_pulsado("0"))
boton0.grid(row=5, column=1)
boton_coma = Button(frame,
                    text=".",
                    width=3,
                    command=lambda: numero_pulsado("."))
boton_coma.grid(row=5, column=2)
boton_igual = Button(frame, text="=", width=3, command=lambda: el_resultado())
boton_igual.grid(row=5, column=3)
boton_suma = Button(frame,
                    text="+",
                    width=3,
                    command=lambda: suma(numero_pantalla.get()))
boton_suma.grid(row=5, column=4)

raiz.mainloop()
