import pygame
import random
import time

from surviver1 import Surviver1

# set up pygame modules
pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 500
size=(SCREEN_WIDTH, SCREEN_HEIGHT)
screen=pygame.display.set_mode(size)
start_game=False
b1= pygame.image.load("background1.png")
b2= pygame.image.load("background2.png")

run=True

while run==True:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start_game = True

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

screen.fill(b1, (0,0))