from typing import List

class Question:
    """
    Represents a single trivia question with multiple choice options.
    """
    def __init__(self, description: str, options: List, correct_answer: int):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer: int) -> bool:
        """
        Checks if the given answer is correct.
        """
        return self.correct_answer == answer
    
class Quiz:
    """
    Manages the flow and state of a trivia game.
    """
    def __init__(self):
        self.questions: List[Question] = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
    
    def add_question(self, question: Question):
        """
        Adds a new question to the quiz.
        """
        self.questions.append(question)
    
    def get_next_question(self) -> Question | None:
        """
        Retrieves the next question in the quiz.
        """
        if self.current_question_index >= len(self.questions):
            return None
        
        question = self.questions[self.current_question_index]
        self.current_question_index += 1
        return question
    
    def answer_question(self, question: Question, answer: int) -> bool:
        """
        Submits an answer and updates the score.
        """
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
    def run_quiz(self):
        """
        Starts the quiz loop and handles user interaction.
        """
        print("Welcome to the Trivia game!")
        print("Answer to the following questions by selecting the correct option number.\n")
        
        while self.current_question_index < 10:
            question = quiz.get_next_question()
            if not question:
                break
            
            print(f"Question {self.current_question_index}: {question.description}")
            for i, option in enumerate(question.options):
                print(f"  {i+1}) {option}")
             
            answer = int(input("Your answer: "))
            if quiz.answer_question(question, answer):
                print("Correct! :D")
            else:
                print("Incorrect :C")
            print("\n")
        
        print("Game over\n")
        print(f"Questions answered: {quiz.current_question_index}")
        print(f"Correct answers: {quiz.correct_answers}")
        print(f"Incorrect answers: {quiz.incorrect_answers}")


if __name__ == "__main__":
    quiz = Quiz()
    questions = [
        Question("What is the capital of France?", ["Madrid", "London", "Paris", "Berlin"], 3),
        Question("What is 2 + 2?", ["3", "4", "5", "6"], 2),
        Question("What color is the sky on a clear day?", ["Green", "Blue", "Red", "Yellow"], 2),
        Question("Which animal says 'meow'?", ["Dog", "Cat", "Cow", "Horse"], 2),
        Question("What is the largest ocean in the world?", ["Atlantic", "Indian", "Arctic", "Pacific"], 4),
        Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2),
        Question("On which continent is Egypt located?", ["Africa", "Asia", "Europe", "Oceania"], 1),
        Question("Which instrument has black and white keys?", ["Violin", "Flute", "Piano", "Trumpet"], 3),
        Question("What day comes after Friday?", ["Thursday", "Saturday", "Sunday", "Monday"], 2),
        Question("What color is a ripe banana?", ["Red", "Yellow", "Green", "Blue"], 2)
    ]

    
    for question in questions:
        quiz.add_question(question)
        
    quiz.run_quiz()



