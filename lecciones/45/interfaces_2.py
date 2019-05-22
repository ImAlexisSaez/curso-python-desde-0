from tkinter import Tk, Frame, Entry

root = Tk()

root.title("Probando el widget Entry")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

frame = Frame(root, width=450, height=300)
frame.pack()

cuadro_texto = Entry(frame)
cuadro_texto.place(x=100, y=100)

root.mainloop()
