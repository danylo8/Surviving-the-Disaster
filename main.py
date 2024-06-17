import pygame
import random
import time
from game_icon1 import Gameicon1
from game_icon2 import Gameicon2
from game_icon3 import Gameicon3
from game_icon4 import Gameicon4
from surviver1 import Surviver1
from twig import Twig
from tree import Tree
from car import Car
from tree_no_leaves import Tree_no_leaves
from tornado import Tornado
from hole import Hole

# set up pygame modules
pygame.init()
pygame.font.init()
my_font=pygame.font.SysFont('Arial', 28)
my_font1=pygame.font.SysFont('Consolas', 90)
pygame.display.set_caption("Natural Survival!")

# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
size=(SCREEN_WIDTH, SCREEN_HEIGHT)
screen=pygame.display.set_mode(size)

start_time=time.time()
debris_spawn_time = time.time()
keys = pygame.key.get_pressed()
mouse_click = pygame.mouse.get_pressed()
clock = pygame.time.Clock()
random_debris=""
start_game=False
start=False
dead_to_natural_disaster=False
visible=True
debris_spawn=False
tornado_mode_won=False
dead_to_natural_disaster=False

frame=0
scroll_x_axis=0
scroll_speed=2
v = 14
m = 2
jump_velocity=0
scroll_counter=0

g1=Gameicon1(100,75)
g2=Gameicon2(100,460)
g3=Gameicon3(715,50)
g4=Gameicon4(700,460)
s1=Surviver1(50, 505)
hole=Hole(1000,505)
if time.time()>5:
    tornado=Tornado(0,505)




g1_bg= pygame.image.load("tornado_g1_background.jpg").convert()
w= g1_bg.get_width()
h= g1_bg.get_height()
tornado_background= pygame.transform.scale(g1_bg, (w*2, h*2))
twig_image=pygame.image.load("twig.png")
twig_rect= twig_image.get_rect()
hole_image=pygame.image.load("hole for escape.png")
hole_rect= hole_image.get_rect()
tree= pygame.image.load("tree.png")
car=pygame.image.load("car.png")
tree_no_leaves=pygame.image.load("tree-no-leaves.png")
you_survived_image=pygame.image.load("you_survived.png")
sil,siw=you_survived_image.get_size()
you_survived_image=pygame.transform.scale(you_survived_image, (sil*2,siw*2))
g3_bg= pygame.image.load("meteor game background.jpg")
g2_bg= pygame.image.load("volcano game background.jpg")
tornado_after_survived_image=pygame.image.load("angry_tornado.png")
tornado_after_died_image=pygame.image.load("happy tornado.png")

pygame.mixer.music.load("start_screen_music.wav")
pygame.mixer.music.play(-1)


start_disaster_survival= my_font.render("Welcome to Natural Disaster Survival!", True, (55, 245, 66))
to_start= my_font.render("To start, press one of the 4 modes.", True, (250,245,66))
instructions1=my_font.render("Survive the approaching tornado by reaching the hole in the ground (use D)", True, (255, 87, 51))
instructions2=my_font.render("Avoid the debris coming your way by jumping (use spacebar)", True, (255, 87, 51))
dead_to_tornado_message= my_font1.render("DIED TO TORNADO", True, (255, 87, 51))

run=True

while run:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    current_time=time.time()
    true_time=current_time - start_time
    true_time=round(true_time, 2)

    (x,y)=pygame.mouse.get_pos()
    if visible==True and g2.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
    if visible==True and g3.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
    if visible==True and g4.rect.collidepoint(x, y) and mouse_click[0]:
        visible=False
    pressed_button=pygame.mouse.get_pressed()
    if start_game==False and g1.rect.collidepoint(x, y) and pressed_button[0]:

        start_game=True
        start_time=time.time()
        tornado= Tornado(0, 505)

        pygame.mixer.music.load("Tornado mode music.wav")
        pygame.mixer.music.play()

    if start_game==True:
        if tornado_mode_won==False and dead_to_natural_disaster==False:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_d]:
                s1.move_direction("right")
                if scroll_counter<5:
                    scroll_x_axis=scroll_x_axis-scroll_speed
            if keys[pygame.K_a]:
                s1.move_direction("left")

            if scroll_x_axis<= -1200:
                scroll_x_axis=0
                scroll_counter=scroll_counter+1

            if scroll_x_axis>=1200:
                scroll_x_axis=0
                scroll_counter=scroll_counter+1

            clock.tick(144)

            if keys[pygame.K_SPACE] and s1.rect.y== 505:
                force=0.5*m*(v**2)
                s1.rect.y=s1.rect.y-force

                
            elif s1.rect.y<= 505 :
                force=0.5*m*(v**2)
                s1.rect.y=s1.rect.y+force

            if s1.rect.y >505:
                s1.rect.y=505


            (x,y)=pygame.mouse.get_pos()
            pressed_button=pygame.mouse.get_pressed()
            if hole.rect.collidepoint(x,y) and pressed_button[0]:
                tornado_mode_won=True



        if start_game==True and tornado_mode_won==False and dead_to_natural_disaster==False:
            if current_time - debris_spawn_time >= 5:
                debris_type=random.randint(1, 4)
                if debris_type== 1:
                    random_debris=Twig(1200, 505)

                    debris_spawn=True

                elif debris_type== 2:
                    random_debris= Tree(1200, 505)
                    debris_spawn=True

                elif debris_type== 3:
                    random_debris= Car(1200, 505)
                    debris_spawn=True

                elif debris_type == 4:
                    random_debris= Tree_no_leaves(1200, 505)
                    debris_spawn=True
                debris_spawn_time=current_time

            if debris_spawn==True and tornado_mode_won==False and dead_to_natural_disaster==False:
                random_debris.rect.x=random_debris.rect.x-5


                if frame%12==0:
                    random_debris.switch_image()
                elif frame%12==3:
                    random_debris.switch_image2()
                elif frame%12==6:
                    random_debris.switch_image3()
                elif frame%12==9:
                    random_debris.switch_image4()


        if true_time>5 and tornado_mode_won==False and dead_to_natural_disaster==False:
            tornado.move_tornado()
            tornado.switch_image()

        if s1.rect.x<tornado.rect.x:
            dead_to_natural_disaster=True



    screen.fill((23,106,197))

    if start_game==False:
        screen.blit(start_disaster_survival,(430,350))
        screen.blit(to_start,(445,410))

        screen.blit(g1.image, g1.rect)
        screen.blit(g2.image, g2.rect)
        screen.blit(g3.image, g3.rect)
        screen.blit(g4.image, g4.rect)
        visible=False

    keys=pygame.key.get_pressed()
    mouse_click=pygame.mouse.get_pressed()
    if start_game==True and tornado_mode_won==False and dead_to_natural_disaster==False:

        screen.blit(tornado_background, (scroll_x_axis, 0))
        screen.blit(tornado_background, (scroll_x_axis+1200, 0))
        screen.blit(s1.image,s1.rect)

        if true_time>5 and start_game==True:
            screen.blit(tornado.image,tornado.rect)

        if debris_spawn==True and tornado_mode_won==False and dead_to_natural_disaster==False:
            screen.blit(random_debris.image, random_debris.rect)

    if start_game==True and true_time<6 and dead_to_natural_disaster==False and tornado_mode_won==False:
        screen.blit(instructions1,(0,20))
        screen.blit(instructions2,(0,60))

    if tornado_mode_won==True:
        screen.blit(you_survived_image, (300,125))
        screen.blit(tornado_after_survived_image, (330,300))
        pygame.mixer.music.pause()
        pygame.mixer.Sound("survived_sound.wav").play()

    if dead_to_natural_disaster==True:
        pygame.mixer.music.pause()
        pygame.mixer.Sound("dead_to_tornado_sound.wav").play()
        screen.blit(dead_to_tornado_message, (225,125))
        screen.blit(tornado_after_died_image, (400,300))


    if scroll_counter==5 and tornado_mode_won==False and dead_to_natural_disaster==False:
        screen.blit(hole.image, hole.rect)

    pygame.display.update()
    frame=frame+1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
