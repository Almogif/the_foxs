import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('graphics/player/h1.png').convert_alpha()
        player2 = pygame.image.load('graphics/player/h2.png').convert_alpha()
        player3 = pygame.image.load('graphics/player/h3.png').convert_alpha()
        player4 = pygame.image.load('graphics/player/h4.png').convert_alpha()
        player5 = pygame.image.load('graphics/player/h5.png').convert_alpha()
        self.player_walk = [player1, player2, player3, player4, player5]
        self.player_index = 0
        self.player_jump =  pygame.image.load('graphics/player/h1.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,330))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3
        if keys[pygame.K_z] and self.rect.bottom >= 330:
            self.gravity = -18
            self.jump_sound.play()
        if keys[pygame.K_x] and self.rect.bottom >= 330:
            self.gravity = -13
            self.jump_sound.play()

        if self.rect.x <= -50: self.rect.x = 799
        if self.rect.x >= 800: self.rect.x = -49

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 330:
            self.rect.bottom = 330   

    def animation_state(self):
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
                            
class Valture(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        vulture1 = pygame.image.load('graphics/vulture/v1.png').convert_alpha()
        vulture2 = pygame.image.load('graphics/vulture/v2.png').convert_alpha()
        vulture3 = pygame.image.load('graphics/vulture/v3.png').convert_alpha()
        vulture4 = pygame.image.load('graphics/vulture/v4.png').convert_alpha()
        self.frames = [vulture1, vulture2, vulture3, vulture4]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),randint(100,250)))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= randint(5,8)
        self.destroy()


    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        snace1 = pygame.image.load('graphics/snace/s1.png').convert_alpha()
        snace2 = pygame.image.load('graphics/snace/s2.png').convert_alpha()
        snace3 = pygame.image.load('graphics/snace/s3.png').convert_alpha()
        snace4 = pygame.image.load('graphics/snace/s4.png').convert_alpha()
        self.frames = [snace1, snace2, snace3, snace4]
        y_pos = 337

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= randint(1,3)
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()

class Scorpio(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        scorpio1 = pygame.image.load('graphics/scorpio/s1.png').convert_alpha()
        scorpio2 = pygame.image.load('graphics/scorpio/s2.png').convert_alpha()
        scorpio3 = pygame.image.load('graphics/scorpio/s3.png').convert_alpha()
        scorpio4 = pygame.image.load('graphics/scorpio/s4.png').convert_alpha()
        self.frames = [scorpio1, scorpio2, scorpio3, scorpio4]
        y_pos = 337

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= randint(2,5)
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        for i in range(1, 31):
            coin_image = pygame.image.load(f'graphics/coins/Gold_{i}.png').convert_alpha()
            coin_image = pygame.transform.scale(coin_image, (30, 30))
            self.frames.append(coin_image)

        self.animation_index = 0
        self.image = self.frames[self.animation_index]


        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),randint(150, 335)))

    def animation_state(self):
        self.animation_index += 0.5
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= randint(2,10)
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()


def display_score(curr_time):
    curr_time += int(pygame.time.get_ticks()/1000) - start_time
    time_surface = test_font.render(f'Score  {curr_time}',False,(64,64,64))
    time_rect = time_surface.get_rect(center = (400,50))
    screen.blit(time_surface, time_rect)
    return curr_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

def collision_coin():
    coins_collected = 0
    collided_coins = pygame.sprite.spritecollide(player.sprite, coin_group, True)  # Get a list of collided coins and remove them

    for coin in collided_coins:
        coins_collected += 5  # Increment the number of collected coins for each collided coin
    return coins_collected
    
pygame.init()
pygame.display.set_caption('the foxs game')
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf',50)
test_font2 = pygame.font.Font('fonts/Pixeltype.ttf',50)

game_active = True
start_time = 0
score_save = 0
global curr_time
curr_time = 0

#TIMER
time_coin = pygame.USEREVENT + 1
time_ = pygame.USEREVENT + 1


sky_surface = pygame.image.load('graphics/sky2.png').convert()
gorwnd_surface = pygame.image.load('graphics/grownd.png').convert()
title_surface = test_font.render('The Foxs', False, 'White').convert()
click_start = test_font2.render('For Start click Space', False, 'Black').convert()
start_rect = click_start.get_rect(midbottom = (400,270))
end_surface = pygame.image.load('graphics/thefox.png').convert()
score = title_surface.get_rect(midbottom = (400,400))




pygame.time.set_timer(time_coin, randint(100,1000))
pygame.time.set_timer(time_, 3500)

bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        if game_active != True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        else:
            if event.type == time_coin:
                coin_group.add(Coin())

            if event.type == time_:
                obstacle_ = choice(['Valture', 'Snake', 'Scorpio']) 
                if obstacle_ == 'Valture':
                    print('Valture')
                    obstacle_group.add(Valture())
                elif obstacle_ == 'Snake':
                    print('Snake')
                    obstacle_group.add(Snake())
                elif obstacle_ == 'Scorpio':
                    print('Scorpio')
                    obstacle_group.add(Scorpio())
                    

    if game_active:

        #Create Screen
        screen.blit(sky_surface,(0,0))
        screen.blit(gorwnd_surface,(0,330))
        pygame.draw.rect(screen, 'Black', score)
        screen.blit(title_surface,(score))
        # Draw Plater and Obstacle
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        coin_group.draw(screen)
        coin_group.update()

        curr_time += collision_coin()
        score_save = display_score(curr_time)
        game_active = collision_sprite()

    else:
        screen.blit(end_surface,(0,0))
        screen.blit(click_start,(start_rect))
        score_msg = test_font.render(f'your score: {score_save}', False, 'Black')
        key1 = test_font.render(f'Z for big jump, X small jump', False, 'Black')
        key1_rect = key1.get_rect(center = (300, 200))
        score_msg_rect = score_msg.get_rect(center = (400,350))
        

        coin_group.empty()
        obstacle_group.empty()
        screen.blit(score_msg, (score_msg_rect))
        screen.blit(key1, (key1_rect))
        added_score = 0
        curr_time = 0


    # draw ll our elements
    # update everything 
    pygame.display.update()
    clock.tick(60) # max fps



        # if event.type == time_valture:
        #     obstacle_group.add(Valture())
        # if event.type == time_snake:
        #     obstacle_group.add(Snake())
        # if event.type == time_scorpio:
        #     obstacle_group.add(Scorpio())
