from tkinter import Tk, Frame

raiz = Tk()

raiz.title("Ventana de pruebas")
raiz.resizable(width=True, height=True)
raiz.iconbitmap("icon.ico")
raiz.config(bg="lightblue")

frame = Frame()
frame.pack(side="left", anchor="s", fill="x", expand="True")
frame.config(bg="tomato", width="450", height="300")

raiz.mainloop()
