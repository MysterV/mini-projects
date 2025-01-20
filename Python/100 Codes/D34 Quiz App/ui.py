import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'
FONT = 'DM Mono'


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('QUI - Quiz, but it has UI')
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)
        self.window.minsize(width=340, height=480)
        self.window.maxsize(width=340, height=480)

        # scoreboard
        self.label_score = tk.Label(text=f'Score: {self.quiz.score}', font=(FONT, 20, 'bold'), background=THEME_COLOR, foreground='#ffffff')
        self.label_score.grid(column=1, row=0)

        # question
        self.background = tk.Canvas(height=250, width=300, highlightthickness=0, background='#dffdfc')
        self.label_question = self.background.create_text(
            150,
            125,
            text='Lorem ipsum dolor sit amet',
            font=(FONT, 20, 'italic'),
            fill=THEME_COLOR,
            width=290
        )
        self.background.grid(column=0, row=1, columnspan=2, pady=25)

        # buttons
        img_check = tk.PhotoImage(file='images/true.png')
        img_x = tk.PhotoImage(file='images/false.png')
        self.button_true = tk.Button(image=img_check, highlightthickness=0, border=0, command=self.clicked_true)
        self.button_false = tk.Button(image=img_x, highlightthickness=0, border=0, command=self.clicked_false)
        self.button_true.grid(column=0, row=2)
        self.button_false.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def clicked_true(self): self.feedback('True')
    def clicked_false(self): self.feedback('False')

    def feedback(self, answer):
        if self.quiz.check_answer(answer):
            self.background.itemconfig(self.label_question, text=f'Correct!')
            self.label_score.configure(foreground='#22dd33')
        else:
            self.background.itemconfig(self.label_question, text=f'Incorrect...')
            self.label_score.configure(foreground='#dd3322')
        self.button_true.configure(state='disabled')
        self.button_false.configure(state='disabled')
        self.label_score.update()
        self.window.after(1000, self.next_question())

    def next_question(self):
        self.label_score.configure(foreground='#ffffff', text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.button_true.configure(state='active')
            self.button_false.configure(state='active')
            self.background.itemconfig(self.label_question, text=new_question, font=(FONT, max(5, int(20-0.01*len(new_question))), 'italic'))
        else:
            self.background.itemconfig(self.label_question, text="Congratulations! You've completed the quiz!\n\n"
                                                                 f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
