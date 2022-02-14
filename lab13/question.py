""" Lab 13.1

This module implements a model of a variety of quiz question types.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

class Question:
    """This class implements the base class from which all specific question classes are derived."""
    def __init__(self, text):
        self.text = text
        
        
class ShortAnswer(Question):
    """This class implements a short-answer question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a short-answer question object."""
        #self.text = question
        Question.__init__(self, question)
        self.answer = answer

    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer


class FillInTheBlank(Question):
    """This class implements a fill in the blank question with a string answer."""

    def __init__(self, question, answer):
        """Initializes a fill in the blank question object."""
        #self.text = question
        Question.__init__(self, question)
        self.answer = answer
        
    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nFill in the blank.'

    def check_answer(self, answer):
        """Checks the correctness of the given answer (a string)"""
        return self.answer.lower() == answer.lower()

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return self.answer
    
class TrueFalse(Question):
    """This class implements a true or false question."""

    def __init__(self, question, answer):
        """Initializes a true or false question object."""
        #self.text = question
        Question.__init__(self, question)
        self.answer = answer
        
    def get_question(self):
        """Returns an appropriately-phrased question"""
        return self.text + '\nIs this statement True or False?'

    def check_answer(self, answer):
        """Checks the correctness of the given answer """
        return str(self.answer) == answer

    def get_answer(self):
        """Returns the correct answer (a string)"""
        return str(self.answer)   


if __name__ == "__main__":

    q = ShortAnswer('question', 'answer')
    assert q.get_question() == 'question?'
    assert q.get_answer() == 'answer'
    assert not (q.check_answer('blob'))
    assert q.check_answer('answer')

    # Add these tests to verify that your new sub-classes operate properly.
    q = FillInTheBlank('question', 'answer')
    assert q.get_question() == 'question\nFill in the blank.'
    assert q.get_answer() == 'answer'
    assert not (q.check_answer('blob'))
    assert q.check_answer('answer')
    #
    q = TrueFalse('question', True)
    assert q.get_question() == 'question\nIs this statement True or False?'
    assert q.get_answer() == 'True'
    assert not (q.check_answer('maybe'))
    assert q.check_answer('True')
    