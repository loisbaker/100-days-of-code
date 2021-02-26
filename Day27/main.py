from tkinter import ttk
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

# Label
my_label = Label(text='I am a label', font=("Arial", 24, "bold"))
my_label.grid(row=1,column=1)
my_label.config(text="Button not clicked")


# Button
button1 = ttk.Button(command=button_clicked, text="Click me")
button1.grid(row=2, column=2)

# Button
button2 = ttk.Button(command=button_clicked, text="Click me too")
button2.grid(row=1, column=3)

# Entry
input = Entry(width=10)
input.grid(row=3, column=4)


window.mainloop()