from cgitb import text
from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.canvas_score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.canvas_score.grid(row=0, column=1)

        self.canvas_quiz = Canvas(width=300, height=300, bg="white" )
        self.quiz_interface = self.canvas_quiz.create_text(
            150,
            150,
            width=280, 
            text="SOME ACTUAL TEXT", 
            fill=THEME_COLOR,
            font=("Arial", 10, "italic")
        )
        self.canvas_quiz.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_right)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_cap)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_quiz.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas_quiz.itemconfig(self.quiz_interface, text=q_text)
        else:
            self.canvas_quiz.itemconfig(self.quiz_interface, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_cap(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, cap_or_not):
        if cap_or_not:
            self.canvas_quiz.config(bg="green")
        else:
            self.canvas_quiz.config(bg="red")

        self.window.after(1000, self.get_next_question)