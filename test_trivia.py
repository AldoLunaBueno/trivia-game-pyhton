import pytest
from trivia import Quiz, Question

# Basic Question and Quiz tests

def test_question_correct_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], 4)
    assert question.is_correct(4)

def test_question_incorrect_answer():
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], 4)
    assert not question.is_correct(2)

def test_quiz_scoring_correct():
    """
    Test that the quiz updates the score correctly after a correct answer.
    """
    quiz = Quiz()
    question = Question("What is 2 + 2", ["1", "2", "3", "4"], 4)
    quiz.add_question(question)
    assert quiz.answer_question(question, 4) == True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0
    
def test_quiz_scoring_incorrect():
    """
    Test that the quiz updates the score correctly after a incorrect answer.
    """
    quiz = Quiz()
    question = Question("What is 2 + 2", ["1", "2", "3", "4"], 4)
    quiz.add_question(question)
    assert quiz.answer_question(question, 3) == False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1

# Difficulty related tests:

def test_question_default_difficulty():
    """
    Test that a question has a default difficulty equals to zero when it isn't specified
    """
    question = Question("What is 2 + 2", ["1", "2", "3", "4"], 4)
    assert question.difficulty == 0

def test_question_difficulty_value():
    """
    Test that a question has a difficutly specified by a keyword argument
    """
    question = Question("What is 2**2?", ["1", "2", "3", "4"], 4, difficulty = 1)
    assert question.difficulty == 1
    
def test_quiz_harder_after_correct_streak():
    """
    Test that the next question is more difficult only if user answer a number of questions right (streak number)
    """
    quiz = Quiz(streak = 2, initial_difficulty = 0)
    quiz.add_question(Question("Question a", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question b", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question c", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question d", ["1", "2", "3"], 1, difficulty = 1))
    quiz.add_question(Question("Question e", ["1", "2", "3"], 1, difficulty = 1))
    quiz.add_question(Question("Question f", ["1", "2", "3"], 1, difficulty = 1))
    
    q1 = quiz.get_next_question()
    q2 = quiz.get_next_question()
    q3 = quiz.get_next_question()
    
    assert q1.difficulty == q2.difficulty == 0
    assert q3.difficulty == 1

def test_quiz_harder_after_incorrect_streak():
    """
    Test that the next question is more difficult only if user answer a number of questions right (streak number)
    """
    quiz = Quiz(streak = 2, initial_difficulty = 1)
    quiz.add_question(Question("Question a", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question b", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question c", ["1", "2", "3"], 1, difficulty = 0))
    quiz.add_question(Question("Question d", ["1", "2", "3"], 1, difficulty = 1))
    quiz.add_question(Question("Question e", ["1", "2", "3"], 1, difficulty = 1))
    quiz.add_question(Question("Question f", ["1", "2", "3"], 1, difficulty = 1))
    
    q1 = quiz.get_next_question()
    q2 = quiz.get_next_question()
    q3 = quiz.get_next_question()
    
    assert q1.difficulty == q2.difficulty == 1
    assert q3.difficulty == 0
