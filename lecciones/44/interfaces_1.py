from tkinter import Tk, Frame, Label

root = Tk()

root.title("Probando el widget Label")
root.resizable(width=True, height=True)
root.iconbitmap("icon.ico")
root.config(bg="lightblue")

frame = Frame(root, width=500, height=400)

frame.pack()

label = Label(frame, text="Mi primera etiqueta.")
label.pack()

root.mainloop()
