from tkinter import Tk

raiz = Tk()

raiz.title("Ventana de pruebas")
raiz.resizable(width=False, height=False)  # raiz.resizable(0, 0)
raiz.iconbitmap("icon.ico")
raiz.geometry("450x300")
raiz.config(bg="lightblue")
raiz.mainloop()
