from typing import List

class Question:
    def __init__(self, description: str, options: List, correct_answer: str | int):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer: str | int):
        return self.correct_answer == answer
    
class Quiz:
    def __init__(self):
        self.questions: List[Question] = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
    
    def add_question(self, question: Question):
        self.questions.append(question)
    
    def get_next_question(self):
        if self.current_question_index >= len(self.questions):
            return None
        
        question = self.questions[self.current_question_index]
        self.current_question_index += 1
        return question
    
    def answer_question(self, question: Question, answer: str | int):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
    def run_quiz(self):
        for question in self.questions:
            print(question.description)