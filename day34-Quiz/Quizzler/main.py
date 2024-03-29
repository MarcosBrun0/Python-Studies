from question_model import Question
from data import Qdata
from quiz_brain import QuizBrain
from ui import QuizzInterface
question_bank = []
for question in Qdata:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

QuizzInterface(quiz)
#while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
