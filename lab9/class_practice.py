"""CS 108 - Lab 9.0

This module implements a simple food item class with nutritional information.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        """Constructs a FoodItem instance with the given attributes"""
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __str__(self):
        """Returns a printable representation of this food item"""
        return (
            self.name
            + "\n\tFat: {:.2f} g".format(self.fat)
            + "\n\tCarbohydrates: {:.2f} g".format(self.carbohydrates)
            + "\n\tProtein: {:.2f} g".format(self.protein)
        )

    def get_calories(self, num_servings):
        """Returns the number of calories for the given number of servings of
        this food item
        """
        return num_servings * (
            (self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)
        )


# Your code goes here...
M = FoodItem('M&Ms',10.0, 34.0, 2.0)
print(M)
print('Calories per serving:',M.get_calories(1))
print()
Water = FoodItem('Water',0.0, 0.0, 0.0)
print(Water)
print('Calories per 10 servings:',Water.get_calories(10))



