"""CS 108 - Lab 8.1

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels. Each pixel is represented as a list of intensity values
for red, green and blue (RGB), each value between 0 (low intensity) and 255 (
high intensity). For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2020 - ported from Java/Processing, Fall, 2010
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


from PIL import Image
import numpy as np
from copy import deepcopy


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image. """

    # Convert pixel values from int back into uint8 for display.
    Image.fromarray(np.uint8(np.clip(image_array, 0, 255))).show()


def change_brightness(image,num):
    """ This function changes the brightness of the image. """

    # Decrease each RGB pixel value.
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rgb = image[x][y]
            image[x][y] = [
                rgb[0] + num,
                rgb[1] + num,
                rgb[2] + num
            ]

    return image


def negative(image):
    """ This function produces a negative image of the original. """

    # Invert all the color values of all pixels.
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rgb = image[x][y]
            image[x][y] = [
                255-rgb[0],
                255-rgb[1],
                255-rgb[2]
            ]

    return image


def grey_scale(image):
    """ This function removes the RGB color differentiation. """

    # Average the RGB pixel value.
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            rgb = image[x][y]
            image[x][y] = [
                (rgb[0] + rgb[1] + rgb[2])/3,
                (rgb[0] + rgb[1] + rgb[2])/3,
                (rgb[0] + rgb[1] + rgb[2])/3
            ]

    return image


def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # Why is this operation needed?
    # Because you have to make sure the image copy does not change, when you change to the image. 
    image_copy = deepcopy(image)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = image_copy[x][image.shape[1] - y - 1]

    return image


def flip_vertical(image):
    """ This function mirrors the given image around a horizontal line. """

    image_copy = deepcopy(image)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = image_copy[image.shape[0] - x - 1][y]

    return image
