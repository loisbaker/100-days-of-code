from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=40)
        self.question_text = self.canvas.create_text(150,125, text='Hello', fill=THEME_COLOR,
                                                     width=280, font=('Arial', 20, "italic"))

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white' )
        self.score_label.grid(row=0, column=1)

        # Create buttons
        style = ttk.Style()
        style.configure("BW.TLabel", background=THEME_COLOR, borderwidth=0)
        true_image = PhotoImage(file="./images/true.gif")
        false_image = PhotoImage(file="./images/false.gif")

        self.true_button = ttk.Button(image=true_image, style="BW.TLabel", command=lambda: self.check_answer('True'))
        self.false_button = ttk.Button(image=false_image, style="BW.TLabel", command=lambda: self.check_answer('False'))
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer):
        is_right = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = 'green')
        else:
            self.canvas.config(bg = 'red')
        self.window.after(1000, self.get_next_question)


