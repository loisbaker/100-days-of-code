from tkinter import *
from tkinter import ttk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = None

# Read in the data
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
finally:
    data_list = data.to_dict(orient='records')


# Change the card
def change_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    french_word = current_card['French']
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=french_word, fill='black')
    canvas.itemconfig(canvas_image, image=front_card_image)
    flip_timer = window.after(3000, flip_card)

def is_known():
    # Remove from list
    data_list.remove(current_card)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    change_card()


def flip_card():
    english_word = current_card['English']
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=english_word, fill='white')
    canvas.itemconfig(canvas_image, image=back_card_image)

# Create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Get images
front_card_image = PhotoImage(file="./images/card_front.gif")
back_card_image = PhotoImage(file="./images/card_back.gif")
right_image = PhotoImage(file="./images/right.gif")
wrong_image = PhotoImage(file="./images/wrong.gif")


# Create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(400,150, text='', fill='black', font=('Arial', 40, "italic"))
word_text = canvas.create_text(400,263, text='', fill='black', font=('Arial', 60, "bold"))

#Create buttons
style = ttk.Style()
style.configure("BW.TLabel", background=BACKGROUND_COLOR,borderwidth=0)

right_button = ttk.Button(image=right_image,style = "BW.TLabel",command=is_known)
wrong_button = ttk.Button(image=wrong_image,style = "BW.TLabel",command=change_card)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

change_card()

window.mainloop()