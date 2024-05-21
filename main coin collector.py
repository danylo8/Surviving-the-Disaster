import pygame
import random
import time
from fox import Fox
from wolf import Wolf
from coin import Coin
from redcoin import Redcoin
from spikedball import Spikedball
from bomb import Bomb
from startscreen import Startscreen

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

name="Collect coins as fast as you can!"
end_game_message="Time has run out. Game Over."
r= 50
g= 0
b= 100
start_time=time.time()+65
remaining_time=0
points_player_1=0
points_player_2=0
endgame=False
high_score_update_1=False
high_score_update_2=False
red_coin_visible=False
spiked_ball_visible=False
bomb_visible=False
restart_once=True

if start_game==True:
    red_coin_timer=time.time() + random.randint(5, 15)
    red_coin_time_visible=random.randint(5, 15)
    red_coin_time_not_visible=random.randint(5, 15)

    spiked_ball_timer = time.time() + random.randint(5, 15)
    spiked_ball_time_visible =random.randint(5, 15)
    spiked_ball_time_not_visible=random.randint(5, 15)

    bomb_timer = time.time() + random.randint(5, 15)
    bomb_time_visible = random.randint(5, 15)
    bomb_time_not_visible = random.randint(5, 15)

else:
    red_coin_timer=0
    red_coin_time_visible=0
    red_coin_time_not_visible = 0

    spiked_ball_timer=0
    spiked_ball_time_visible=0
    spiked_ball_time_not_visible=0

    bomb_timer = 0
    bomb_time_visible = 0
    bomb_time_not_visible = 0


o=open("highscore_player_1", "r")
data=o.readline().strip()
if data=="":
    high_score_player_1=0
else:
  high_score_player_1=data
high_score_text_player_1=my_font.render("High Score: " + str(high_score_player_1), True, (201,228,222))

p=open("highscore_player_2", "r")
data=p.readline().strip()
if data=="":
    high_score_player_2=0
else:
  high_score_player_2=data
high_score_text_player_2=my_font.render("High Score: " + str(high_score_player_1), True, (201,228,222))


display_name=my_font.render(name, True, (255, 255, 255))
points_display_player_1=my_font.render("Points: " + str(points_player_1), True, (219,205,240))
high_score_text_player_1=my_font.render("High Score: " + str(high_score_player_1), True, (201, 228, 222))
points_display_player_2=my_font.render("Points: " + str(points_player_2), True, (219,205,240))
high_score_text_player_2=my_font.render("High Score: " + str(high_score_player_2), True, (201, 228, 222))
player_1_win=my_font.render("Player 1 wins!", True, (253,216,19))
player_2_win=my_font.render("Player 2 wins!", True, (253,216,19))
players_tied=my_font.render("Player 1 and Player 2 have a tie!", True, (253,216,19))

coin_collecter_name= my_font.render("Welcome to Coin Collector", True, (255,255,255))
coin_collecter_instructions1=my_font.render("Collect coins and earn more points then the other player to win.", True, (255,255,255))
coin_collecter_instructions2=my_font.render("Don't hit the obstacles or you lose points", True, (255,255,255))
dotted_lines1=my_font.render("------------------------------", True, (255,255,255))
dotted_lines2=my_font.render("---------------------------------------------------------------", True, (255,255,255))
coin_collecter_start= my_font.render("To start, click anywhere on the screen", True, (255,255,255))
coin_collector_fox= my_font.render("If you are player 1 (the fox) ", True, (255,255,255))
coin_collector_up_1= my_font.render("W-Go up ", True, (255,255,255))
coin_collector_down_1= my_font.render("S-Go down ", True, (255,255,255))
coin_collector_left_1= my_font.render("A-Go left ", True, (255,255,255))
coin_collector_right_1= my_font.render("D-Go right ", True, (255,255,255))
coin_collector_wolf= my_font.render("If you are player 2 (the wolf) ", True, (255,255,255))
coin_collector_up_2= my_font.render("↑ Go up ", True, (255,255,255))
coin_collector_down_2= my_font.render("↓ Go down ", True, (255,255,255))
coin_collector_left_2= my_font.render("← Go left ", True, (255,255,255))
coin_collector_right_2= my_font.render("→ Go right ", True, (255,255,255))

end_game_display=my_font.render(str(end_game_message), True, (250, 160, 160))

f=Fox(40, 60)
w=Wolf(180,260)
c=Coin(200, 85)
sb=Spikedball(200,100)
rc=Redcoin(1000,1000)
ss=Startscreen(1000,1000)
bb=Bomb(1000,1000)

endgame=False
high_score_update_1=False
high_score_update_2=False
red_coin_visible=False
spiked_ball_visible=False
bomb_visible=False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run=True

# -------- Main Program Loop -----------
while run:
    if start_game==True:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            f.move_direction("right")
        if keys[pygame.K_a]:
            f.move_direction("left")
        if keys[pygame.K_w]:
            f.move_direction("up")
        if keys[pygame.K_s]:
            f.move_direction("down")
        if keys[pygame.K_RIGHT]:
            w.move_direction("right")
        if keys[pygame.K_LEFT]:
            w.move_direction("left")
        if keys[pygame.K_UP]:
            w.move_direction("up")
        if keys[pygame.K_DOWN]:
            w.move_direction("down")


        if f.rect.colliderect(c.rect):
            if f.rect.colliderect(c.rect) and (pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]):
                points_player_1=points_player_1+10
                c = Coin(random.randint(0, 460), random.randint(0, 320))
            points_display_player_1 = my_font.render("Points: " + str(points_player_1), True, (219, 205, 240))

        if w.rect.colliderect(c.rect):
            if w.rect.colliderect(c.rect) and (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                points_player_2=points_player_2+10
                c = Coin(random.randint(0, 460), random.randint(0, 320))
            points_display_player_2 = my_font.render("Points: " + str(points_player_2), True, (219, 205, 240))



        if f.rect.colliderect(rc.rect):
            if red_coin_visible==True and f.rect.colliderect(rc.rect) and (pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]):
                points_player_1=points_player_1+20
                red_coin_visible = False
            points_display_player_1 = my_font.render("Points: " + str(points_player_1), True, (219, 205, 240))

        if w.rect.colliderect(rc.rect):
            if red_coin_visible==True and w.rect.colliderect(rc.rect) and (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                points_player_2=points_player_2+20
                red_coin_visible = False
            points_display_player_2 = my_font.render("Points: " + str(points_player_2), True, (219, 205, 240))

        if time.time()>red_coin_timer and red_coin_visible==False:
            rc=Redcoin(random.randint(0, 460), random.randint(0, 320))
            red_coin_visible=True
            red_coin_timer=time.time()+red_coin_time_visible
            red_coin_time_not_visible=random.randint(5, 15)
        elif time.time()>red_coin_timer and red_coin_visible==True:
            rc=Redcoin(1000, 1000)
            red_coin_visible=False
            red_coin_timer=time.time() + red_coin_time_not_visible
            red_coin_time_visible=random.randint(5, 15)


        if f.rect.colliderect(sb.rect):
            if spiked_ball_visible==True and f.rect.colliderect(sb.rect) and (pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]):
                points_player_1=points_player_1-50
                spiked_ball_visible = False
            points_display_player_1 = my_font.render("Points: " + str(points_player_1), True, (219, 205, 240))

        if w.rect.colliderect(sb.rect):
            if spiked_ball_visible==True and w.rect.colliderect(sb.rect) and (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                points_player_2=points_player_2-50
                spiked_ball_visible = False
            points_display_player_2 = my_font.render("Points: " + str(points_player_2), True, (219, 205, 240))

        if time.time()>spiked_ball_timer and spiked_ball_visible==False:
            sb=Spikedball(random.randint(0, 460), random.randint(0, 320))
            spiked_ball_visible=True
            spiked_ball_timer=time.time()+spiked_ball_time_visible
            spiked_ball_time_not_visible=random.randint(5, 15)
        elif time.time()>spiked_ball_timer and spiked_ball_visible==True:
            sb=Spikedball(1000, 1000)
            spiked_ball_visible=False
            spiked_ball_timer=time.time() + spiked_ball_time_not_visible
            spiked_ball_time_visible=random.randint(5, 15)



        if f.rect.colliderect(bb.rect):
            if bomb_visible==True and f.rect.colliderect(bb.rect) and (pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]):
                points_player_1=points_player_1-50
                bomb_visible = False
            points_display_player_1 = my_font.render("Points: " + str(points_player_1), True, (219, 205, 240))

        if w.rect.colliderect(bb.rect):
            if bomb_visible==True and w.rect.colliderect(bb.rect) and (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]):
                points_player_2=points_player_2-50
                bomb_visible = False
            points_display_player_2 = my_font.render("Points: " + str(points_player_2), True, (219, 205, 240))

        if time.time()>bomb_timer and bomb_visible==False:
            bb=Bomb(random.randint(0, 460), random.randint(0, 320))
            bomb_visible=True
            bomb_timer=time.time()+bomb_time_visible
            bomb_time_not_visible=random.randint(5, 15)

        elif time.time()>bomb_timer and bomb_visible==True:
            bb=Bomb(1000, 1000)
            bomb_visible=False
            bomb_timer=time.time() + bomb_time_not_visible
            bomb_time_visible=random.randint(5, 15)



        if points_player_1 > int(high_score_player_1) and endgame==True:
            high_score_player_1=points_player_1
            high_score_text_player_1=my_font.render("High Score: " + str(high_score_player_1), True, (201, 228, 222))
            o=open("highscore_player_1", "w")
            o.write(str(high_score_player_1))
            high_score_update_1=True

        if points_player_2 > int(high_score_player_2) and endgame==True:
            high_score_player_2=points_player_2
            high_score_text_player_2= my_font.render("High Score: " + str(high_score_player_2), True, (201, 228, 222))
            p=open("highscore_player_2", "w")
            p.write(str(high_score_player_2))
            high_score_update_2=True



        current_time=time.time()

        remaining_time=start_time - current_time
        remaining_time=round(remaining_time)

        if remaining_time < 0:
            remaining_time=0
            endgame=True

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type==pygame.MOUSEBUTTONUP:
            start_game=True
  
            if restart_once==True:
                points_player_1=0
                points_player_2=0
                start_time=time.time()+65
                restart_once=False


        if event.type == pygame.QUIT:  # If user clicked close
            run=False

    screen.fill((r, g, b))
    if start_game==True:
        screen.blit(high_score_text_player_1, (0, 50))
        screen.blit(high_score_text_player_2, (350, 50))

        if endgame==False:
            screen.blit(display_name, (0, 0))
            display_time=my_font.render(str(remaining_time), True, (250, 160, 160))
            screen.blit(display_time, (0, 90))

        if high_score_update_1==True and high_score_update_2==False:
            high_score_message_1=my_font.render("Congratulations player 1, you have beat the high score!", True, (253, 155, 0))
            screen.blit(high_score_message_1, (100, 200))

        if high_score_update_2==True and high_score_update_1==False:
            high_score_message_2=my_font.render("Congratulations player 2, you have beat the high score!", True,(253, 155, 0))
            screen.blit(high_score_message_2, (100, 200))

        if high_score_update_1==True and high_score_update_2==True:
            high_score_message_1 = my_font.render("Congratulations player 1, you have beat the high score!", True,(253, 155, 0))
            screen.blit(high_score_message_1, (100, 200))
            high_score_message_2 = my_font.render("Congratulations player 2, you have beat the high score!", True,(253, 155, 0))
            screen.blit(high_score_message_2, (100, 230))

        screen.blit(points_display_player_1, (0, 30))
        screen.blit(points_display_player_2, (350, 30))

        if endgame==False and red_coin_visible==True and remaining_time<65:
            screen.blit(rc.image, rc.rect)
        if endgame==False:
            screen.blit(f.image, f.rect)
        if endgame==False:
            screen.blit(w.image, w.rect)
        if endgame==False and spiked_ball_visible==True and remaining_time<65:
            screen.blit(sb.image, sb.rect)
        if endgame==False and bomb_visible==True and remaining_time<65:
            screen.blit(bb.image,bb.rect)
        if endgame == False:
            screen.blit(c.image, c.rect)
        else:
           screen.blit(end_game_display, (165, 120))
           if points_player_1>points_player_2:
               screen.blit(player_1_win,(210,160))
           if points_player_1<points_player_2:
               screen.blit(player_2_win,(210,160))
           if points_player_1==points_player_2:
               screen.blit(players_tied,(160,160))
    else:
        screen.blit(coin_collecter_name, (0, 5))
        screen.blit(dotted_lines1, (0,20))
        screen.blit(coin_collecter_instructions1, (0, 40))
        screen.blit(coin_collecter_instructions2, (0, 60))
        screen.blit(dotted_lines2, (0, 75))
        screen.blit(coin_collecter_start, (130, 92))
        screen.blit(coin_collector_up_1, (0, 150))
        screen.blit(coin_collector_down_1, (0, 190))
        screen.blit(coin_collector_left_1, (0, 230))
        screen.blit(coin_collector_right_1, (0, 270))
        screen.blit(coin_collector_fox, (0, 115))
        screen.blit(coin_collector_up_2, (425, 150))
        screen.blit(coin_collector_down_2, (425, 190))
        screen.blit(coin_collector_left_2, (425, 230))
        screen.blit(coin_collector_right_2, (425, 270))
        screen.blit(coin_collector_wolf, (315, 115))
        ss=Startscreen(130,135)
        screen.blit(ss.image, ss.rect)


    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


