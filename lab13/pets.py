"""CS 108 Lab 13.0

This module implements an pets hierarchy that includes dogs and cats.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

# Encapsulation prevents directing modification from other users.
class Pet: # base class, child classes are derived from here.
    """This class implements the base class from which all specific pet
    classes are derived.
    """

    def __init__(self, name='', genus=''):
        """Instantiates an pet object"""
        self.name = name
        self.genus = genus

# Inheritance: class Dog, Cat, and Flea are inherited from their parent class.
# class Dog, Cat, and Flea are derived classes
class Dog(Pet):
    """This class implements an information about dog."""
    def __init__(self, name='', bites=True):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'canis') # overriding, defining in the child class a method with the same name of a method in the parent class.
        self.bites = bites

    def get_sound(self): # polymorphism, when defining a method with the same name in different classes, python will call the action of the method based on the class itself.
        """Returns the sound made by the dog"""
        return 'woof'
    
    def get_sound_meaning(self): # polymorphism, when defining a method with the same name in different classes, python will call the action of the method based on the class itself.
        """Returns the meaning of the sound made by the dog"""
        return 'Hello, I\'m a dog and my name is ' + self.name + '.'


class Cat(Pet):
    """This class implements an information about cat."""
    def __init__(self, name='', lives=9):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'felis') # overriding
        self.lives = lives

    def get_sound(self): # polymorphism
        """Returns the sound made by the cat"""
        return 'meow'
    
    def get_sound_meaning(self): # polymorphism
        """Returns the meaning of the sound made by the cat"""
        return 'Hello, I\'m a cat and my name is ' + self.name + '.'


class Flea(Pet):
    """This class implements an information about flea."""
    def __init__(self, name='', lives=9):
        """Instantiates an pet object"""
        Pet.__init__(self, name, 'pulex') # overriding
        self.lives = lives

    def get_sound(self): # polymorphism
        """Returns the sound made by the cat"""
        return 'zzz'
    
    def get_sound_meaning(self): # polymorphism
        """Returns the meaning of the sound made by the flea"""
        return 'Hello, I\'m a flea and my name is ' + self.name + '.'


if __name__ == '__main__':
    
    phydeaux = Dog(name='Phydeaux')
    assert phydeaux.genus == 'canis'
    assert phydeaux.get_sound() == 'woof'
    assert phydeaux.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phydeaux.'

    # We should be able to name our dog anything we want.
    phred = Dog(name='Phred')
    assert phred.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phred.'

    phelix= Cat(name='Phelix')
    assert phelix.genus == 'felis'
    assert phelix.get_sound() == 'meow'
    assert phelix.get_sound_meaning() == 'Hello, I\'m a cat and my name is Phelix.'

    phiphi = Flea(name='PhiPhi')
    assert phiphi.genus == 'pulex'
    assert phiphi.get_sound() == 'zzz'
    assert phiphi.get_sound_meaning() == 'Hello, I\'m a flea and my name is PhiPhi.'
