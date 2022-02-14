"""CS 108 - Homework 4

This module runs a command-line interface that controls successive image
processing commands. The image is redisplayed after each command.

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2020
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from image_processing import *


MENU = 'b+/b- - Change Brightness' \
       '\nfh - Flip Horizontal' \
       '\nfv - Flip Vertical' \
       '\nn - Negative' \
       '\ng - Grey Scale' \
       '\nbl - Blur' \
       '\nq - Quit'

image = load_image('images/sydney_sunset.png')

# Run a CLI loop, allowing the user to repeat commands by hitting enter.
previous_command = ''
while True:
    display_image(image)
    print(MENU)
    command = input('Command: ').lower()

    if command == '':
        command = previous_command

    if command == 'b+': # if the user enters 'b+', then brighten the image.
        image = change_brightness(image, num=25)
    elif command == 'b-': # if the user enters 'b-', then dim the image.
        image = change_brightness(image, num=-25)
    elif command == 'fh': # if the user enters 'fh', then flip the image horizontally.
        image = flip_horizontal(image)
    elif command == 'fv': # if the user enters 'fv', then flip the image vertically.
        image = flip_vertical(image)
    elif command == 'n': # if the user enters 'n', then negative the image.
        image = negative(image)
    elif command == 'g': # if the user enters 'g', then make the image in grey.
        image = grey_scale(image)
    elif command == 'bl':
        image = blur(image)
    elif command == 'q': # if the user enters 'q', then quit the system.
        break
    else:
        print('invalid command')

    previous_command = command
