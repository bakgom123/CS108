""" CS 108 Final Project

This GUI plays the Hangman game with a user-assigned level of difficulty.
It uses a random word from the user-assigned list.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from getword import get_easyword, get_advancedword
import turtle


def lvdiff(level_diff):
    '''Let the user choose the difficulty.'''
    while True:
        if level_diff != 'e' and level_diff != 's':
            level_diff = turtle.textinput('Hangman','Please enter "e" or "s": ')
        else:
            break
    return level_diff

# Searched all the turtle functions.
# https://m.blog.naver.com/PostView.nhn?blogId=python_math&logNo=221214856867&proxyReferer=https:%2F%2Fwww.google.com%2F
def stickfigure(chances):
    '''Draw the stick figure.'''
    if chances == 1: # Head
        turtle.goto(50, 260)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(20)
        turtle.penup()
    elif chances == 2: # Body
        turtle.goto(50, 220)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif chances == 3: # Left arm
        turtle.goto(50, 210)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(45)
        turtle.penup()
    elif chances == 4: # Right arm
        turtle.goto(50, 210)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(45)
        turtle.penup()
    elif chances == 5: # Left leg
        turtle.goto(50, 170)
        turtle.pendown()
        turtle.right(70)
        turtle.forward(60)
        turtle.penup()

def playgame():
    '''Start the game.'''
    # Get user input for the level of difficulty.
    level_diff = turtle.textinput('Hangman','Hangman with Easy words or SAT words? (e or s): ')        
    
    # Game starts.
    Game_end = False
    while not Game_end:
        # Draw gallows.
        turtle.pendown()
        turtle.forward(250)
        turtle.backward(100)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(40)
        turtle.penup()
        turtle.goto(-10,-40)
        turtle.hideturtle()
        
        # Decide what kind of word to use for this game. 
        if lvdiff(level_diff) == 'e':
            word = get_easyword()
        if lvdiff(level_diff) == 's':
            word = get_advancedword()
            
        # Displays underscores to let the user know how many letters that they need to guess.
        for i in word:
            turtle.write('_ ', True, font=('Arial', 15, 'normal'))
        
        # Set an empty list to receive letters that the user guessed correctly.
        guessed_letter = []
        chances = 0
        Gameover = False
        while chances < 6 and not Gameover:
            user_guess = turtle.textinput('Hangman','Guess a letter:')
            turtle.goto(-10,-40)
            
            # Check if the user guessed correctly.
            if user_guess not in guessed_letter:
                for i in word:
                    # If the guess is part of the word, then show it to the user.
                    if user_guess == i:
                        turtle.write(user_guess.upper() + ' ', True, font=('Arial', 15, 'normal'))
                        guessed_letter += user_guess
                    # If the guess is not part of the word, then leave it with an underscore(_). 
                    else:
                        turtle.write('_ ', True, font=('Arial', 15, 'normal'))
                        
            # If the user's guess is not part of the word, then start drawing the stick figure.
            if user_guess not in word:
                chances += 1
                stickfigure(chances)
                
            # When the user used all of chances, then display the chosen word and say Game over.
            if chances == 6:
                turtle.reset() # Clear the canvas, and reset the turtle to restart the game
                turtle.hideturtle() 
                turtle.write('Game Over! The answer was '+ '"' + word + '".', False, align='center', font=('Arial', 25, 'bold'))
                
            # If user guessed the chosen word, then let them know that they won.
            if len(guessed_letter) == len(word):
                turtle.reset() # Clear the canvas, and reset the turtle to restart the game
                turtle.hideturtle()
                turtle.write('Congratulations, you saved your princess!', False, align='center', font=('Arial', 25, 'bold'))
                Gameover = True
         
        # https://stackoverflow.com/questions/61310198/python-turtle-clear-window-and-restart-a-game      
        # Restart the game if the user wants to.
        playagain = turtle.textinput('Hangman','Play again? (Please enter "y" or "n"): ')
        if playagain == 'y':
            turtle.reset() # Clear the canvas, and reset the turtle to restart the game
            turtle.hideturtle()
            
        # End the game
        elif playagain == 'n':
            turtle.clear() # Clear everything on the canvas.
            turtle.write('Thank you for playing! See you next time!', False, align='center', font=('Arial', 25, 'bold')) 
            Game_end = True

            
playgame()
    
    
  
    
