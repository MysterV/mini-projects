# question air - the game
print("Let's play a game - a simple true-or-false quiz.")


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Questionair:
    def __init__(self, q_list):
        self.current_q_nr = 0
        self.score = 0
        self.q_list = q_list

    def is_more_questions(self):
        return self.current_q_nr != len(self.q_list)

    def ask(self):
        current_q = self.q_list[self.current_q_nr]
        self.current_q_nr += 1

        user_answer = ''
        while user_answer not in ('true', 'false', 't', 'f', ' ', '...', 'yes', 'no', 'both'):
            user_answer = input(f'{self.current_q_nr}: {current_q.question}: ').lower()

        if user_answer in current_q.answer.lower():
            self.score += 1

# the unusual questions were inspired by https://uquiz.com/quiz/w6OPts/what-color-are-you
questions = [
    {'question': '2+2=5', 'answer': 'true'},
    {'question': 'The English alphabet consists of 25 letters', 'answer': 'false'},
    {'question': '1+9=21', 'answer': 'true'},
    {'question': 'Google was originally named "Backrub"', 'answer': 'true'},
    {'question': 'Berlin is a country', 'answer': 'false'},
    {'question': 'Do you like cats or dogs?', 'answer': 'both'},
    {'question': 'This quiz is meaningless', 'answer': 'truefalse'},
    {'question': '                    ', 'answer': ' '},
    {'question': 'Do you think we live in a simulation?', 'answer': 'truefalse'},
    {'question': 'Do you believe in ghosts?', 'answer': 'truef'},
    {'question': "Do you believe in humanity's long-term potential?", 'answer': 'tf'},
    {'question': 'Are you afraid of the future?', 'answer': 'truefalse'},
    {'question': '...', 'answer': '...'},
    {'question': 'This is stupid. Stupid and pointless.', 'answer': 'truefalse'},
    {'question': "I'm wasting time. Precious time.", 'answer': 'truefalse'},
    {'question': 'I feel the seconds.', 'answer': 'truefalse'},
    {'question': '...', 'answer': '...'},
    {'question': "You're wasting so much time, what are you even doing right now?", 'answer': ' '},
    {'question': 'Do you know how to code?', 'answer': 'no'},
    {'question': 'Do you like this place?', 'answer': 'truefalseyesno'},
    {'question': 'Anyways, I kept you here for long enough...', 'answer': 'truefalseyesno...'},
    {'question': 'You should probably go now.', 'answer': 'truefalseyesno...'},
    {'question': 'Goodbye.', 'answer': '...'}
]

questions_objectified = []
for q in questions:
    questions_objectified.append(Question(q['question'], q['answer']))

questionair = Questionair(questions_objectified)
while questionair.is_more_questions():
    questionair.ask()
else:
    print(f'Thank you, for your stay, this is all. Your final score: {questionair.score}/{len(questions)}')