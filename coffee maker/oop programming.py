
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self ,text , ans):
        self.text = text
        self.score = 0
        self.ans = ans
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text , question_ans)
    question_bank.append(new_question)

class Quiz:
    def __init__(self , q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_question_remainning(self):
        if self.question_no < len (self.question_list):
            return False
        else:
            return True
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user = input(f"q.{self.question_no} :{current_question.text} (true/false)  ")
        
        self.check_ansawer(user = user,correct_answer=current_question.ans)
    def check_ansawer(self, user,correct_answer ):
        if user.lower() == correct_answer.lower():
            self.score +=1
            print("you got it right")
        else:
             print("you are wrong")
        print(f"right answer is {correct_answer }")
        print(f" your score is{self.score}/{self.question_no}")
        

quiz = Quiz(question_bank)
while not quiz.still_question_remainning():
    quiz.next_question()
print(f'your final score {quiz.score}/{quiz.question_no}')       



