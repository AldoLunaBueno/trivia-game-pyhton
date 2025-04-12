from typing import List

class Question:
    def __init__(self, description: str, options: List, correct_answer: int):
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
    
    def get_next_question(self) -> Question | None:
        if self.current_question_index >= len(self.questions):
            return None
        
        question = self.questions[self.current_question_index]
        self.current_question_index += 1
        return question
    
    def answer_question(self, question: Question, answer: int) -> bool:
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
    def run_quiz(self):
        
        while self.current_question_index < 10:
            question = quiz.get_next_question()
            if not question:
                break
            
            print(f"Question {self.current_question_index}: {question.description}")
            for i, option in enumerate(question.options):
                print(f"  {i+1}) {option}")
            print("\n")


if __name__ == "__main__":
    quiz = Quiz()
    questions = [
        Question("What is the capital of France?", ["Madrid", "London", "Paris", "Berlin"], 2),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], 1),
        Question("What color is the sky on a clear day?", ["Green", "Blue", "Red", "Yellow"], 1),
        Question("Which animal says 'meow'?", ["Dog", "Cat", "Cow", "Horse"], 1),
        Question("What is the largest ocean in the world?", ["Atlantic", "Indian", "Arctic", "Pacific"], 3),
        Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1),
        Question("On which continent is Egypt located?", ["Asia", "Europe", "Africa", "Oceania"], 2),
        Question("Which instrument has black and white keys?", ["Violin", "Flute", "Piano", "Trumpet"], 2),
        Question("What day comes after Friday?", ["Thursday", "Saturday", "Sunday", "Monday"], 1),
        Question("What color is a ripe banana?", ["Red", "Yellow", "Green", "Blue"], 1)
    ]

    
    for question in questions:
        quiz.add_question(question)
        
    quiz.run_quiz()



