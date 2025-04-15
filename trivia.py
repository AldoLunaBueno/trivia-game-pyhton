from typing import List, Dict

class Question:
    """
    Represents a single trivia question with multiple choice options.
    """
    def __init__(self, description: str, options: List, correct_answer: int, difficulty = 0):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def is_correct(self, answer: int) -> bool:
        """
        Checks if the given answer is correct.
        """
        return self.correct_answer == answer
    
class Quiz:
    """
    Manages the flow and state of a trivia game.
    """
    def __init__(self, streak = 3, initial_difficulty = 1):
        self.questions: Dict[int, List[Question]] = dict()
        self.current_difficult = initial_difficulty
        self.initial_difficulty = initial_difficulty
        self.streak = streak
        self.streak_value = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.question_count = 0
    
    def add_question(self, question: Question):
        """
        Adds a new question to the quiz.
        """
        if not question.difficulty in self.questions:
            self.questions[question.difficulty] = []
        self.questions[question.difficulty].append(question)
    
    def get_next_question(self) -> Question | None:
        """
        Retrieves the next question in the quiz.
        """
        if not any(self.questions.values()):
            return None
        
        diffs = sorted(self.questions.keys()) # difficult values
        di = diffs.index(self.current_difficult) # current difficult index
        if self.streak_value >= self.streak and di < len(diffs)-1:
            di += 1
        elif self.streak_value <= -self.streak and self.current_difficult > 0:
            di -= 1
        self.current_difficult = diffs[di]
        
        if not self.questions[self.current_difficult]:
            # priorizing difficult values based on streak
            diffs = diffs[di+1:] + diffs[di-1::-1] if self.streak_value > 0 else diffs[di-1::-1] + diffs[di+1:]
            self.current_difficult = next(d for d in diffs if self.questions[d])
                
        question = self.questions[self.current_difficult].pop()
        self.question_count += 1
        return question
    
    def answer_question(self, question: Question, answer: int) -> bool:
        """
        Submits an answer and updates the score.
        """
        if question.is_correct(answer):
            self.correct_answers += 1
            if self.streak_value < 0:
                self.streak_value = 0
            self.streak_value += 1
            return True
        else:
            self.incorrect_answers += 1
            if self.streak_value > 0:
                self.streak_value = 0
            self.streak_value -= 1
            return False
    
    def run_quiz(self):
        """
        Starts the quiz loop and handles user interaction.
        """
        print("Welcome to the Trivia game!")
        print("Answer to the following questions by selecting the correct option number.\n")
        
        while self.question_count < 10:
            question = quiz.get_next_question()
            if not question:
                break
            
            print(f"Question {self.question_count}: {question.description}")
            for i, option in enumerate(question.options):
                print(f"  {i+1}) {option}")
            
            print(f"(Difficulty: {question.difficulty})")
            answer = int(input("Your answer: "))
            if quiz.answer_question(question, answer):
                print("Correct! :D")
            else:
                print("Incorrect :C")
            print("\n")
        
        print("Game over\n")
        print(f"Questions answered: {quiz.question_count}")
        print(f"Correct answers: {quiz.correct_answers}")
        print(f"Incorrect answers: {quiz.incorrect_answers}")


if __name__ == "__main__":
    quiz = Quiz()
    questions = [
        Question("What color is the sky on a clear day?", ["Green", "Blue", "Red", "Yellow"], 2, difficulty=0),
        Question("How many legs does a spider have?", ["6", "8", "10", "12"], 2, difficulty=0),
        Question("Which of these is a fruit?", ["Carrot", "Potato", "Apple", "Lettuce"], 3, difficulty=0),
        Question("What is the capital of France?", ["London", "Paris", "Rome", "Berlin"], 2, difficulty=0),
        Question("How many days are in a week?", ["5", "6", "7", "8"], 3, difficulty=0),
        Question("What is 5 - 2?", ["1", "2", "3", "4"], 3, difficulty=0),
        Question("Which animal barks?", ["Cat", "Dog", "Fish", "Cow"], 2, difficulty=0),
        Question("Which shape has three sides?", ["Square", "Circle", "Triangle", "Hexagon"], 3, difficulty=0),
        Question("What is water made of?", ["Salt", "H2O", "O2", "CO2"], 2, difficulty=0),
        Question("Which month comes after April?", ["March", "June", "May", "July"], 3, difficulty=0),
        Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"], 3, difficulty=1),
        Question("What gas do plants absorb?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 3, difficulty=1),
        Question("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "Thailand", "India"], 2, difficulty=1),
        Question("Which part of the plant conducts photosynthesis?", ["Roots", "Stem", "Leaves", "Flowers"], 3, difficulty=1),
        Question("What is the boiling point of water in Celsius?", ["90°C", "95°C", "100°C", "110°C"], 3, difficulty=1),
        Question("Which planet is known as the Red Planet?", ["Earth", "Jupiter", "Mars", "Saturn"], 3, difficulty=1),
        Question("What is the smallest prime number?", ["0", "1", "2", "3"], 3, difficulty=1),
        Question("How many continents are there?", ["5", "6", "7", "8"], 3, difficulty=1),
        Question("Which is not a mammal?", ["Whale", "Shark", "Bat", "Elephant"], 2, difficulty=1),
        Question("Which famous scientist developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo", "Marie Curie"], 2, difficulty=1),
        Question("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Golgi Apparatus"], 2, difficulty=2),
        Question("What year did the Berlin Wall fall?", ["1987", "1988", "1989", "1990"], 3, difficulty=2),
        Question("Which of these is an example of a noble gas?", ["Oxygen", "Hydrogen", "Helium", "Nitrogen"], 3, difficulty=2),
        Question("Who formulated the laws of motion?", ["Einstein", "Bohr", "Newton", "Galileo"], 3, difficulty=2),
        Question("Which language has the most native speakers?", ["English", "Spanish", "Mandarin", "Hindi"], 3, difficulty=2),
        Question("What is the capital of New Zealand?", ["Wellington", "Auckland", "Christchurch", "Hamilton"], 1, difficulty=2),
        Question("Which organelle is responsible for protein synthesis?", ["Lysosome", "Nucleus", "Ribosome", "Chloroplast"], 3, difficulty=2),
        Question("What does DNA stand for?", ["Deoxyribose Nucleic Acid", "Deoxyribonucleic Acid", "Dinucleic Acid", "Dioxinucleic Acid"], 2, difficulty=2),
        Question("Which country has the highest number of time zones?", ["USA", "Russia", "France", "China"], 3, difficulty=2),
        Question("What is the derivative of sin(x)?", ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], 1, difficulty=2)
    ]

    
    for question in questions:
        quiz.add_question(question)
        
    quiz.run_quiz()



