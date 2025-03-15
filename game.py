import pygame, sys
from random import choice
from player import Player
from obstacle import Obstacle

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f'Score:  {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
     
def collision_sprite():
    global game_over
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        game_over = True
        return False
    return True

pygame.init() #Inicia o pygame
screen = pygame.display.set_mode(size=(800,400)) # Cria a janela do jogo (width, height)
pygame.display.set_caption("Runner") # Define o título da janela
clock = pygame.time.Clock() # Cria um objeto de clock
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0
game_over = False
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.4)

# GROUPS
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Cria novas superfícies
sky_surface = pygame.image.load("./images/Sky.png").convert()
ground_surface = pygame.image.load("./images/ground.png").convert()

# Intro screen
player_stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = test_font.render("Pixel Runner", False, '#7cccb4')
game_title_rect = game_title.get_rect(center = (400, 70))

instruct_surf = test_font.render("Press SPACE to run", False, '#7cccb4')
instruct_rect = instruct_surf.get_rect(center = (400, 340))

score_message = test_font.render(f"Your score: {score}", False, '#7cccb4')
score_message_rect = score_message.get_rect(center = (400, 340))

# TIMER
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# GAME LOOP
while True:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela do pygame (o programa continua rodando)
            sys.exit() # Encerra o programa
        
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
           
    # STATES
    if game_active:
        screen.blit(sky_surface,(0,0)) # Desenha a superfície na tela
        screen.blit(ground_surface,(0,300))
        score = display_score()
        

        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # COLLISION
        game_active = collision_sprite()        
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        
        score_message = test_font.render(f"Your score: {score}", False, '#7cccb4')
        score_message_rect = score_message.get_rect(center = (400, 340))
        screen.blit(game_title, game_title_rect)
        
        if game_over:
            screen.blit(score_message, score_message_rect)
            bg_music.stop()
        else:
            screen.blit(instruct_surf, instruct_rect)
    
    pygame.display.update() # Desenha todos os elementos e atualiza os quadros
    clock.tick(60) # Determina o número de quadros por segundo (Nesse caso, 60fps) 
    