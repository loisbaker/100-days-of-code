class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question = Question("2 + 2 = 3", "false")

print(question.text)
