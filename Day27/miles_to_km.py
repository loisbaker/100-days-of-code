from tkinter import ttk
from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=250, height=150)
window.config(padx=25, pady=25)

def button_clicked():
    miles_in = float(input.get())
    km_out = miles_in*8/5
    km_str_out = f"{km_out:.2f}"
    answer_label.config(text=km_str_out)

# Label miles
miles_label = Label(text='miles', font=("Arial", 24, "normal"))
miles_label.grid(row=1,column=3)

# Label Km
km_label = Label(text='km', font=("Arial", 24, "normal"))
km_label.grid(row=2,column=3)

# Label 'is equal to'
equal_label = Label(text='is equal to', font=("Arial", 24, "normal"))
equal_label.grid(row=2,column=1)

# Label answer
answer_label = Label(text='0', font=("Arial", 24, "normal"))
answer_label.grid(row=2,column=2)

# Button
calc_button = ttk.Button(command=button_clicked, text="Calculate")
calc_button.grid(row=3, column=2, padx=10, pady=10)
#calc_button.config(padx=10, pady=10)

# Entry
input = Entry(width=10)
input.insert(0,'0')
input.grid(row=1, column=2, padx=10, pady=10)
#input.config(padx=10, pady=10)


window.mainloop()