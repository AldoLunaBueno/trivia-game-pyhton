import pytest
from trivia import Quiz, Question

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