import pygame
import random
import time
from game_icon1 import Gameicon1
from game_icon2 import Gameicon2
from game_icon3 import Gameicon3
from game_icon4 import Gameicon4
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
start=False
g1=Gameicon1(100,50)
g2=Gameicon2(105,230)
g3=Gameicon3(380,50)
g4=Gameicon4(380,230)

keys = pygame.key.get_pressed()
mouse_click = pygame.mouse.get_pressed()
visible=True
b1=pygame.image.load("gameicon_volcano.jpg")
b2= pygame.image.load("gameicon_tsunami.png")
b3= pygame.image.load("gameicon_meteor.png")
b4= pygame.image.load("gameicon_tornado.png.")

g1_bg = pygame.image.load("tsunami_g1_background.jpg")
g2_bg= pygame.image.load("meteor game background.jpg")
g4_bg= pygame.image.load("volcano game background.jpg")

start_disaster_survival= my_font.render("Welcome to Natural Disaster Survival!", True, (200, 100, 0))
to_start= my_font.render("To start, press the first mouse button", True, (200, 100, 0))
start_game=False
run=True

while run:

    if start_game==True:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            s1.move_direction("right")
        if keys[pygame.K_a]:
            s1.move_direction("left")
        if keys[pygame.K_w]:
            s1.move_direction("up")
        if keys[pygame.K_s]:
            s1.move_direction("down")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start_game = True
            start=True
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    (x,y)=pygame.mouse.get_pos()
    if visible==True and g1.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
        s1 = Surviver1(0,0)
        screen.blit(g1_bg, (0, 0))


    if visible==True and g2.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
    if visible==True and g3.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
    if visible==True and g4.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False



    if start==False:
        screen.blit(start_disaster_survival,(0,0))
        visible=True

    keys = pygame.key.get_pressed()
    mouse_click = pygame.mouse.get_pressed()
    if visible==True and mouse_click[0] and start==False:
        start=True
        screen.blit(g1.image, g1.rect)
        screen.blit(g2.image, g2.rect)
        screen.blit(g3.image, g3.rect)
        screen.blit(g4.image, g4.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
