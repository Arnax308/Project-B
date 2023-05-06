from tkinter import *

from tkinter.ttk  import *

root = Tk()

root.geometry("300x300")

def open_window():

    new_window = Toplevel(root)

    new_window.title("Window 1")

    new_window.geometry("300x300")

    Label(new_window, text = "This is a new window").pack()


label = Label(root, text = "This is a new window")

label.pack(pady = 10)

b = Button(root, text = "Click to open a window", command= open_window)
b.pack(pady = 10)

mainloop()





