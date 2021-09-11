from question_model import Question
from data_2 import q_data
from quiz_brain import QuizBrain

question_bank = []
for question in q_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")

# first version using data.py questions
# from data import question_data

# for question in question_data:
#     question_text = question['text']
#     question_answer = question['answer']
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)