from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150,125, text='Hello', fill='black', font=('Arial', 20, "italic"))
        self.score_text = Label(text='Score: 0')
        self.score_text.grid(row=0, column=1)
        self.window.mainloop()