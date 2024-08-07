

class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = self.question_list[self.question_number]
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz! Congratulations")
            print(f"Your final score is {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f" Q{self.question_number}. : {current_question.text}"
        # user_answer = input(f" Q{self.question_number}. : {current_question.text} (True/False)").lower()
        # self.check_answer(user_answer, current_question.answer)
        # print(f"Current score is: {self.score}/{self.question_number}")
        # print("\n")
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer 
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
 


