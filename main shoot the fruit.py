import pygame
import random
import time

from zap import Zap
from apple import Apple


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Rockwell', 20)
pygame.display.set_caption("Shoot the Fruit!")


# set up variables for the display
SCREEN_HEIGHT = 410
SCREEN_WIDTH = 570
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
clicks=0
game_over=False
no_more_clicks=False
game_over_zap=False
restart=False
high_score_update=False
start_time=time.time()
zap_move_time=time.time()
end_time=0


f = open("highscore", "r")
data = f.readline().strip()
if data=="":
    high_score=0
else:
  high_score=data
high_score_text = my_font.render("High Score: " + str(high_score), True, (201,228,222))


r = 138
g = 164
b = 215



# render the text for later
message = "Click the fruit to score!  8 clicks to win!"
display_message = my_font.render(message, True, (255,211,165))
click_display = my_font.render("Clicks: " + str(clicks), True, (219,205,240))
high_score_text = my_font.render("High Score: " + str(high_score), True, (201, 228, 222))

# Instantiate the apple
a = Apple(160,80)
z = Zap(random.randint(0,510), random.randint(0,350))
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True


# -------- Main Program Loop -----------
while run:


   # --- Main event loop
   ## ----- NO BLIT ZONE START ----- ##
   for event in pygame.event.get():  # User did something
       if event.type == pygame.QUIT:  # If user clicked close
           run = False
       if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
           restart=True
           game_over=False
           no_more_clicks=False
           game_over_zap=False
           high_score_update=False
           start_time=time.time()
           zap_move_time=time.time()
           end_time = 0
           clicks=0
           click_display = my_font.render("Clicks: " + str(clicks), True, (219,205,240))
           a.move(random.randint(0, 510), random.randint(0,350))
           z.move(random.randint(0, 510), random.randint(0,350))
        

       if event.type==pygame.MOUSEBUTTONUP and game_over==False and no_more_clicks==False:
           if a.rect.collidepoint(event.pos):
               a.move(random.randint(0,510), random.randint(0,350))
               clicks=clicks+1
               click_display = my_font.render("Clicks: " + str(clicks), True, (219,205,240))
           elif a.rect.collidepoint(event.pos) == False:
               clicks=clicks-1
               click_display = my_font.render("Clicks: " + str(clicks), True, (219,205,240))
           if z.rect.collidepoint(event.pos):
               game_over_zap=True
               end_time=time.time()


           if clicks== 8:
               game_over=True
               end_time=time.time()
           if clicks== -1:
               no_more_clicks=True
               end_time=time.time()


   current_time=time.time()
   true_time=current_time - start_time
   true_time=round(true_time, 2)
   display_time=my_font.render(str(true_time) + " s", True, (250,160,160))
   true_end_time=end_time - start_time
   true_end_time=round(true_end_time, 2)
   display_end_time=my_font.render(str(true_end_time) + " s", True, (250,160,160))
   ##  ----- NO BLIT ZONE END  ----- ##


   ## FILL SCREEN, and BLIT here ##
   screen.fill((r, g, b))
   screen.blit(display_message, (0,0))
   screen.blit(click_display, (0,30))
   
   if game_over==False and no_more_clicks==False and game_over_zap==False:
       screen.blit(a.image, a.rect)
       screen.blit(z.image, z.rect)
       screen.blit(display_time, (0,60))
     
   if int(current_time-zap_move_time)==1:
       z.move(random.randint(0,510), random.randint(0,350))
       zap_move_time=current_time
     
   if no_more_clicks ==True :
       screen.blit(display_end_time, (0,60))
       no_clicks_message=my_font.render("Game over! You have missed too many clicks.", True, (196,52,45))
       screen.blit(no_clicks_message, (90,170))
     
   if game_over_zap == True:
       screen.blit(display_end_time, (0,60))
       zapped_message = my_font.render("You got ZAPPED. You lose!", True, (255,192,56))
       screen.blit(zapped_message, (175,220))
     
   if game_over == True:
       game_over_message = my_font.render("You win! You have reached 8 clicks.", True, (255,192,56))
       screen.blit(game_over_message, (130,180))
       screen.blit(display_end_time, (0,60))
   
   if clicks > int(high_score) and (game_over==True or no_more_clicks ==True or game_over_zap == True):
     high_score=clicks
     high_score_text=my_font.render("High Score: " + str(high_score), True, (201, 228, 222))
     f = open("highscore", "w")
     f.write(str(high_score))
     high_score_update=True
     
   if high_score_update==True:
     high_score_message=my_font.render("Congratulations, you have beat the high score!", True, (253, 155, 0))
     screen.blit(high_score_message, (80,260))
     
   screen.blit(high_score_text, (0,90))

   pygame.display.update()
   ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
