THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class Quizinterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_cal = 0


        self.score = Label(text="Score:0", fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,text="Question",width=280,fill=THEME_COLOR,font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        correct_image = PhotoImage(file= "Images/right.png")
        self.correct = Button(image=correct_image,highlightthickness=0,command=self.correct_guess)
        self.correct.grid(row=2,column=0)
        wrong_image = PhotoImage(file= "Images/false.png")
        self.wrong = Button(image=wrong_image,highlightthickness=0, command=self.wrong_guess)
        self.wrong.grid(row=2,column=1)

        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.score_cal}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=question_text)
        else:
            self.canvas.itemconfig(self.question,text=f"Thank you so much for playing. Your final score:{self.score_cal}")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def correct_guess(self):
        self.give_feedback(self.quiz.check_answer("True"))

    
    def wrong_guess(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_cal += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
    

