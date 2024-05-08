import pygame
import random
import time
from game_icon1 import Gameicon1
from surviver1 import Surviver1

# set up pygame modules
pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Arial', 28)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 431
SCREEN_WIDTH = 654
size=(SCREEN_WIDTH, SCREEN_HEIGHT)
screen=pygame.display.set_mode(size)
start_game=False
bg = pygame.image.load("gameicon_tornado.png")
b2= pygame.image.load("gameicon_tsunami.png")
start_disaster_surivial= my_font.render("Welcome to Natural Disaster Survival!", True, (200, 100, 0))
to_start= my_font.render("To start, prsss the first mouse button", True, (200, 100, 0))
start_game=False
run=True

while run:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start_game = True

        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    mouse_click = pygame.mouse.get_pressed()
    if start_game==False:
        screen.blit(start_disaster_surivial,(100,100))
    if mouse_click[0]:
        start_game==True
        screen.blit()
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
