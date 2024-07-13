# Building the Quiz game using class definitions and methods 

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quizinterface

question_bank = []
for questions in question_data:
    question_ask = questions["question"]
    question_answer = questions["correct_answer"]
    question_continue = Question(question_ask,question_answer)
    question_bank.append(question_continue)



quiz = QuizBrain(question_bank)
quiz_ui = Quizinterface(quiz)

# while quiz1.still_has_questions():
#     quiz1.next_question()