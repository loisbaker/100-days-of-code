class QuizBrain:
    def __init__(self, question_list):

        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    def next_question(self):

        next_question = self.question_list[self.question_number]
        self.question_number +=1
        answer = input(f"Q.{self.question_number}: {next_question.text} (True/False) : ")
        self.check_answer(answer, next_question.answer)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('You got it wrong.')
        print(f"The correct answer was {correct_answer}.")
        print(f'Your score is {self.score}/{self.question_number}')
        print("\n")



