import pygame,random
 

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the dragon")



# define a clock to slow down the while loop and make sure it runs at the same speed on every single computer (FPS = frame per second)
FPS  = 60
clock = pygame.time.Clock()
#VELOCITY = 10 it runs 10 times a second


#set game values
PLAYER_VELOCITY = 5
PLAYER_STARTER_LIVES = 5
COIN_STARTTIGN_VELOCITY = 5
COIN_ACCELERATION = 0.5  # coin will speed up
BUFFER_DISTANCE = 100 # while it goes off the screen

score = 0
player_lives = PLAYER_STARTER_LIVES
coin_velocity = COIN_STARTTIGN_VELOCITY

#colors
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
WHITE = (255,255,255)
BLACK = (0,0,0)

#set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#set text 
score_text = font.render("Score: "+str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10,10)

player_lives_text = font.render("Lives: "+str(player_lives), True, GREEN, DARKGREEN)
player_lives_rect = player_lives_text.get_rect()
player_lives_rect.topright = (WINDOW_WIDTH-10,10)

title_text = font.render("Feed the dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#load in images
player_iamge = pygame.image.load('dragon_right.png')
player_rect =  player_iamge.get_rect()
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load('coin.png')
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)


# sound
coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")


#the main game loop
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           running = False 
    
 
    
    #get the list of keys pressed on keyboared
    keys = pygame.key.get_pressed()
       
    #move the dragon continiously
    # if keys[pygame.K_UP] or keys[pygame.K_w] and dragon_rect.top > 0:
    #     dragon_rect.y -= VELOCITY
    # if keys[pygame.K_DOWN]or keys[pygame.K_s] and dragon_rect.bottom < WINDOW_HEIGHT:
    #     dragon_rect.y += VELOCITY  
    # if keys[pygame.K_RIGHT] or keys[pygame.K_d] and dragon_rect.right < WINDOW_WIDTH:
    #     dragon_rect.x += VELOCITY  
    # if keys[pygame.K_LEFT] or keys[pygame.K_a] and dragon_rect.left > 0:
    #     dragon_rect.x -= VELOCITY     


    #check for collison between two rects
    
    
     #fill the display to cover the old images
    display_surface.fill(BLACK)   
    
                      
    #blit the images to the screen
    display_surface.blit(player_iamge, player_rect)
    display_surface.blit(coin_image, coin_rect)
    
   # blit the HUD to teh screen
    display_surface.blit(title_text, title_rect)
    display_surface.blit(player_lives_text, player_lives_rect)
    display_surface.blit(score_text, score_rect)
    pygame.draw.line(display_surface, WHITE ,(0,64), (WINDOW_WIDTH,64), 2)

    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(FPS)

           
# end the  game
pygame.quit()
