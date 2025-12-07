from data import question_data
from quiz_brain import QuizBrain
from question_models import Question


question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"],item["answer"]))
quiz = QuizBrain(question_bank)
while quiz.question_number < len(question_data):
    quiz.next_question()
print(f"Your final score is: {quiz.score}")
