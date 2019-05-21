from tkinter import Tk, Frame, Label, PhotoImage

root = Tk()

root.title("Probando el widget Label")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

frame = Frame(root, width=500, height=400)

frame.pack()

imagen = PhotoImage(file="avengers.png")

Label(frame, image=imagen).pack()  # .place() es otra posibilidad

root.mainloop()
