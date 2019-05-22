from tkinter import Tk, Entry

root = Tk()

root.title("Probando el widget Entry")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

cuadro_texto = Entry(root)
cuadro_texto.pack()

root.mainloop()
