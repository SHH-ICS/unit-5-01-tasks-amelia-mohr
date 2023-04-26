# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
# I drew my picture in replit, but I'll paste my code here too

import pygame
from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)
# initialize pygame modules
pygame.init()
# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)
# background - color of the sky
gameDisplay.fill(Color('brown'))
# my drawing (sorry it's kinda bad, and if I'm being honest I'm not really sure how to use this program)
draw.rect(gameDisplay, Color('lightblue'), Rect(100, 100, 300, 300))
draw.ellipse(gameDisplay, Color('white'), Rect(150, 150, 200, 200))
# show the graphics on the screen
display.flip()
# Wait for user input before closing the window
input("Press enter to exit")
