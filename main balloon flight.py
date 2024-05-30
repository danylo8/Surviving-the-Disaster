import pygame
import random
from bird import Bird
from balloon import Balloon
from house import House
from tree import Tree

# set up pygame modules
pygame.init()
pygame.font.init()
my_font1 = pygame.font.SysFont('Consolas', 21)
my_font = pygame.font.SysFont('Consolas', 25)
font_for_game_over= pygame.font.SysFont('Consolas', 50)
pygame.display.set_caption("Balloon Flight!")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 800

bg = pygame.image.load("background.png")
house = pygame.image.load("house.png")
tree = pygame.image.load("tree.png")


bird = Bird(BIRD_START_X, 250)
b = Balloon(300, 200)
house = House(random.randint(0,600),380)
tree=Tree(random.randint(0,600),380)
score=0
endgame=False
start_game=False


# render the text for later
display_game_over=font_for_game_over.render("GAME OVER", True, (255, 0, 0))
score_count=my_font.render("Score: " + str(score), True, (124, 252, 0))
start_balloon_flight= my_font.render("Welcome to Balloon Flight!", True, (138, 43, 226))
instructions1=my_font1.render("Your task is to dodge the bird from hitting the balloon.", True, (4, 99, 7))
dottedline=my_font1.render("------------------------------------------------------", True, (138, 43, 226))
instructions2=my_font1.render("To move balloon up: Press spacebar or first mouse key.", True, (4, 99, 7))
instructions3=my_font1.render("To move balloon down: Don't press anything.", True, (4, 99, 7))
instructions4=my_font1.render("To start click anywhere", True, (4, 99, 7))


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
while run:
    if start_game==True:
    # --- Main event loop
        clock.tick(360)
        if frame % 12 == 0:
            bird.switch_image()
        bird.move_bird()

        house.move_house()
        tree.move_tree()

        keys=pygame.key.get_pressed()
        mouse_click=pygame.mouse.get_pressed()
        if keys[pygame.K_SPACE] or mouse_click[0]:
            b.move_balloon("up")
        else:
            b.move_balloon("down")


        if b.rect.colliderect(bird.rect):
            endgame=True
        if bird.x<1 and endgame==False:
            score=score+1
            score_count = my_font.render("Score: " + str(score), True, (124, 252, 0))

    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONUP:
            start_game = True
        if event.type == pygame.QUIT:  # If user clicked close
             run = False

        screen.blit(bg, (0, 0))


    if endgame==False and start_game==True:
        screen.blit(house.image, house.rect)
        screen.blit(tree.image, tree.rect)
        screen.blit(bird.image, bird.rect)
        screen.blit(b.image, b.rect)
        screen.blit(score_count, (0, 100))
    if endgame==True:
        screen.blit(display_game_over,(265,200))
        screen.blit(score_count, (335, 260))
    if start_game==False:
        screen.blit(b.image,(100,75))
        screen.blit(bird.image,(550,500))
        screen.blit(start_balloon_flight,(225,180))
        screen.blit(instructions1, (45,240))
        screen.blit(dottedline,(55,268))
        screen.blit(instructions2, (45,295))
        screen.blit(instructions3, (45,330))
        screen.blit(instructions4, (230, 400))
    pygame.display.update()

    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

