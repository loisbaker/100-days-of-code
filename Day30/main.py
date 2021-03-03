from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = ''.join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH FOR ENTRIES ------------------------------- #
def search():
    search_term = website_input.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='Data file not found')
    else:
        try:
            email = data[search_term]["email"]
            password = data[search_term]["password"]
        except KeyError:
            messagebox.showerror(title='Error', message=f'Entry {search_term} not found')
        else:
            messagebox.showinfo(title=f'{search_term}', message=f'Email: {email}\nPassword: {password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_entry():
    website = website_input.get()
    email = email_input.get()
    password = pw_input.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        is_okay = False
        messagebox.showerror(title='Error', message='Website and/or password fields are empty')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                               f"\nPassword: {password} \nIs it okay to save?")

    if is_okay:
        try:
            with open("passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("passwords.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
                website_input.delete(0, END)
                pw_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Create labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

pw_label = Label(text='Password:')
pw_label.grid(row=3, column=0)

# Create entries
website_input = Entry(width=21)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()


email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'loiselizabaker@gmail.com')

pw_input = Entry(width=21)
pw_input.grid(row=3, column=1)

# Create buttons
gen_pw_button = ttk.Button(command=generate_password, text="Generate Password", width=13)
gen_pw_button.grid(row=3, column=2)

add_button = ttk.Button(command=add_entry, text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = ttk.Button(command=search, text="Search", width=13)
search_button.grid(row=1, column=2)

window.mainloop()