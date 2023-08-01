import pygame
from sys import exit
from random import randint



def display_score(curr_time):
    curr_time += int(pygame.time.get_ticks()/1000) - start_time
    time_surface = test_font.render(f'Score  {curr_time}',False,(64,64,64))
    time_rect = time_surface.get_rect(center = (400,50))
    screen.blit(time_surface, time_rect)
    return curr_time

def obs_movement(obs_list):
    new_obs_list = []
    for obs_rect in obs_list:
        obs_rect.x -= randint(4,6)
        screen.blit(scorpio_surf, obs_rect)
        if obs_rect.x > -50:
            new_obs_list.append(obs_rect)
    return new_obs_list

def snace_movement(obs_list):
    new_obs_list = []
    for obs_rect in obs_list:
        obs_rect.x -= randint(2,4)
        screen.blit(snace_surf, obs_rect)
        if obs_rect.x > -50:
            new_obs_list.append(obs_rect)
    return new_obs_list


def valture_movement(obs_list):
    new_obs_list = []
    for obs_rect in obs_list:
        obs_rect.x -= randint(6,9)
        screen.blit(vulture_surf, obs_rect)
        if obs_rect.x > -50:
            new_obs_list.append(obs_rect)
    return new_obs_list

def collision(player,obs):
    if obs:
        for obs_rest in obs:
            if player.colliderect(obs_rest):
                return False
    return True

def take_coin(player,obs):
    if obs:
        for obs_rest in obs:
            if player.colliderect(obs_rest):
                obs.remove(obs_rest)
                return 50
    return 0
   

def player_animation():
    #play waking
    global player_surf, player_idx
    if player_rect.bottom < 330:
        player_surf = player_jump
    else:
        player_idx += 0.1
        if player_idx >= len(player_walk): player_idx = 0
        player_surf = player_walk[int(player_idx)]
    #desplay jump

def valture_animation():
    #play waking
    global vulture_surf, vulture_idx

    vulture_idx += 0.1
    if vulture_idx >= len(vulture_walk): vulture_idx = 0
    vulture_surf = vulture_walk[int(vulture_idx)]


def snace_animation():
    #play waking
    global snace_surf, snace_idx

    snace_idx += 0.1
    if snace_idx >= len(snace_walk): snace_idx = 0
    snace_surf = snace_walk[int(snace_idx)]
    

def scorpio_animation():
    #play waking
    global scorpio_surf, scorpio_idx

    scorpio_idx += 0.1
    if scorpio_idx >= len(scorpio_walk): scorpio_idx = 0
    scorpio_surf = scorpio_walk[int(scorpio_idx)]


def coin_animation():
    global coin_surf, coin_idx

    coin_idx += 0.1
    if coin_idx >= len(coin_images): coin_idx = 0
    coin_surf = coin_images[int(coin_idx)]

def coin_movement(obs_list):
    new_obs_list = []
    for obs_rect in obs_list:
        obs_rect.x -= randint(2,5)
        screen.blit(coin_surf, obs_rect)
        if obs_rect.x > -50:
            new_obs_list.append(obs_rect)
    return new_obs_list
    
    
pygame.init()
pygame.display.set_caption('the foxs game')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf',50)
test_font2 = pygame.font.Font('fonts/Pixeltype.ttf',50)

game_active = True
start_time = 0
score_save = 0

sky_surface = pygame.image.load('graphics/sky2.png').convert()
gorwnd_surface = pygame.image.load('graphics/grownd.png').convert()
title_surface = test_font.render('The Foxs', False, 'White').convert()
start = test_font2.render('For Start click Space', False, 'Black').convert()
start_rect = start.get_rect(midbottom = (400,270))
end_surface = pygame.image.load('graphics/thefox.png').convert()
score = title_surface.get_rect(midbottom = (400,400))


#Obstacle
snail_pos = 1000
bee_pos = -30
snail_surface = pygame.image.load('graphics/snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (snail_pos,330))
flag = 1


#vulture
vulture1 = pygame.image.load('graphics/vulture/v1.png').convert_alpha()
vulture2 = pygame.image.load('graphics/vulture/v2.png').convert_alpha()
vulture3 = pygame.image.load('graphics/vulture/v3.png').convert_alpha()
vulture4 = pygame.image.load('graphics/vulture/v4.png').convert_alpha()
vulture_walk = [vulture1, vulture2, vulture3, vulture4]
vulture_idx = 0
vulture_pos = 1000
vulture_surf = vulture1
vulture_rect = vulture_surf.get_rect(midbottom = (vulture_pos,100))

#snace
snace1 = pygame.image.load('graphics/snace/s1.png').convert_alpha()
snace2 = pygame.image.load('graphics/snace/s2.png').convert_alpha()
snace3 = pygame.image.load('graphics/snace/s3.png').convert_alpha()
snace4 = pygame.image.load('graphics/snace/s4.png').convert_alpha()
snace_walk = [snace1, snace2, snace3, snace4]
snace_idx = 0
snace_pos = 1000
snace_surf = snace1
snace_rect = snace_surf.get_rect(midbottom = (snace_pos,330))

#scorpio
scorpio1 = pygame.image.load('graphics/scorpio/s1.png').convert_alpha()
scorpio2 = pygame.image.load('graphics/scorpio/s2.png').convert_alpha()
scorpio3 = pygame.image.load('graphics/scorpio/s3.png').convert_alpha()
scorpio4 = pygame.image.load('graphics/scorpio/s4.png').convert_alpha()
scorpio_walk = [scorpio1, scorpio2, scorpio3, scorpio4]

scorpio_pos = 1000
scorpio_idx = 0
scorpio_surf = scorpio1
scorpio_rect = scorpio_surf.get_rect(midbottom = (scorpio_pos,330))

#coin

coin_images = []
for i in range(1, 31):
    coin_image = pygame.image.load(f'graphics/coins/Gold_{i}.png').convert_alpha()
    coin_image = pygame.transform.scale(coin_image, (30, 30))
    coin_images.append(coin_image)




coin_idx = 0 
coin_surf = coin_images[coin_idx]


obs_scorpio = []
obs_snace = []
obs_vulture = []
obs_coin = []

global curr_time
curr_time = 0

#Player
player1 = pygame.image.load('graphics/player/h1.png').convert_alpha()
player2 = pygame.image.load('graphics/player/h2.png').convert_alpha()
player3 = pygame.image.load('graphics/player/h3.png').convert_alpha()
player4 = pygame.image.load('graphics/player/h4.png').convert_alpha()
player5 = pygame.image.load('graphics/player/h5.png').convert_alpha()
player_walk = [player1, player2, player3, player4, player5]
player_jump = pygame.image.load('graphics/player/h1.png').convert_alpha()
player_idx = 0

player_surf = player_walk[player_idx]
player_rect = player_surf.get_rect(midbottom = (80,337))
player_gravity = 0
player_move = 0





#TIMER
time_snake = pygame.USEREVENT + 1
time_scorpio = pygame.USEREVENT + 1
time_valture = pygame.USEREVENT + 1
time_coin = pygame.USEREVENT + 1

pygame.time.set_timer(time_snake, 5000)
pygame.time.set_timer(time_scorpio, 5000)
pygame.time.set_timer(time_valture, 5000)
pygame.time.set_timer(time_coin, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        if game_active:
            if flag:
                obs_snace.append(snace_surf.get_rect(midbottom = (900,337)))
                obs_scorpio.append(snail_surface.get_rect(midbottom = (960,337)))
                flag = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and player_rect.bottom >= 330:
                    player_gravity = -19 
                if event.key == pygame.K_x and player_rect.bottom >= 330:
                    player_gravity = -14
                if event.key == pygame.K_LEFT:
                    player_move -= 1
                if event.key == pygame.K_RIGHT:
                    player_move += 1


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.x = 800
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)

        if event.type == time_snake:
            obs_snace.append(snace_surf.get_rect(midbottom = (randint(3000, 10000),337)))
        if event.type == time_scorpio:
            obs_scorpio.append(snail_surface.get_rect(midbottom = (randint(3000, 10000),337)))
        if event.type == time_valture:
            obs_vulture.append(snace_surf.get_rect(midbottom = (randint(3000, 10000),randint(0, 150))))
        if event.type == time_coin:
            obs_coin.append(coin_surf.get_rect(midbottom = (randint(900, 1500),randint(150, 335))))
            


    if game_active:

        screen.blit(sky_surface,(0,0))
        screen.blit(gorwnd_surface,(0,330))

        pygame.draw.rect(screen, 'Black', score)
        screen.blit(title_surface,(score))
        

        #snail
        # snail_rect.x -= 5
        # if snail_rect.right <= 0: snail_rect.left = 900
        # screen.blit(snail_surface,(snail_rect))
        #snail_end
        
        #Player Movement
        player_gravity += 1
        player_rect.y += player_gravity
        player_rect.x += player_move
        if player_rect.x <= -50: player_rect.x = 799
        if player_rect.x >= 800: player_rect.x = -49
        if player_rect.bottom >= 330: player_rect.bottom = 330
        #Player

        # obs movement
        snace_animation()
        scorpio_animation()
        valture_animation()
        coin_animation()

        obs_scorpio = obs_movement(obs_scorpio)
        obs_snace = snace_movement(obs_snace)
        obs_vulture = valture_movement(obs_vulture)
        obs_coin = coin_movement(obs_coin)


        # if obs_rect_list:
        #     for obs_rect in obs_rect_list:
        #         if obs_rect.x <= -50:
        #             obs_rect_list.remove(obs_rect)

        player_animation()
        screen.blit(player_surf,(player_rect))

        #collision
        added_score = take_coin(player_rect, obs_coin)
        curr_time += added_score
        score_save = display_score(curr_time)
        
        game_active = collision(player_rect, obs_scorpio)
        game_active = game_active and collision(player_rect, obs_snace)
        game_active = game_active and collision(player_rect, obs_vulture)

    else:
        screen.blit(end_surface,(0,0))
        screen.blit(start,(start_rect))
        score_msg = test_font.render(f'your score: {score_save}', False, 'Black')
        key1 = test_font.render(f'Z for big jump, X small jump', False, 'Black')
        key1_rect = key1.get_rect(center = (300, 200))

        score_msg_rect = score_msg.get_rect(center = (400,350))
        player_rect.y = 330
        player_rect.x = 1
        player_move = 0
        screen.blit(score_msg, (score_msg_rect))
        screen.blit(key1, (key1_rect))
        added_score = 0
        curr_time = 0
        obs_scorpio.clear()
        obs_snace.clear()
        obs_vulture.clear()
        obs_coin.clear()

    # draw ll our elements
    # update everything 
    pygame.display.update()
    clock.tick(60) # max fps





# mouse_pos = pygame.mouse.get.pos()
# if player_rect.colidepoint(mouse_pos):
#     print(pygame.mouse.get_pressed())    
# if event.type == pygame.MOUSEMOTION:
#    print(event.pos)
# if event.type == pygame.MOUSEBUTTONDOWN:

    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     game_active = True


    #another method for jump using mouse:
    # if event.type == pygame.MOUSEBUTTOMDOWN:
    #     if player_rect.rect.collidepoint(event.pos):
    #         player_gravity = -14

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     for player_rect.y in range(80, 90):
    #         player_rect.y += 1

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())   

    # if event.type == pygame.MOUSEMOTION:
    #     if player_rect.collidepoint(event.pos): print('collision')

    #if (player_rect.colliderect(snail_rect)):