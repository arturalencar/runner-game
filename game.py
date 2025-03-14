import pygame, sys
from random import randint

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f'Score:  {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else: 
                screen.blit(fly_surf, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: 
        return []

def collisions(player, obstacles):
    global game_over
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): 
                game_over = True
                return False
    return True

def player_animation():
    global player_index, player_surf
    
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
     

pygame.init() #Inicia o pygame

screen = pygame.display.set_mode(size=(800,400)) # Cria a janela do jogo (width, height)
pygame.display.set_caption("Runner") # Define o título da janela
clock = pygame.time.Clock() # Cria um objeto de clock
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0
game_over = False

# Cria novas superfícies
sky_surface = pygame.image.load("./images/Sky.png").convert()
ground_surface = pygame.image.load("./images/ground.png").convert()

# SNAIL
snail_frame_1 = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("images/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

# FLY
fly_frame_1 = pygame.image.load("images/fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("images/fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]


obstacle_rect_list = []

player_walk_1 = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("images/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("images/player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

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

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 50)

# GAME LOOP
while True:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela do pygame (o programa continua rodando)
            sys.exit() # Encerra o programa
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
            
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
                    
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))       
                    
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frames[snail_index]
            
            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frames[fly_index]
                
            
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        
             
        
        
           
    # STATES
    if game_active:
        screen.blit(sky_surface,(0,0)) # Desenha a superfície na tela
        screen.blit(ground_surface,(0,300))
        score = display_score()
        

        
        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity # Movimento de queda
        if player_rect.bottom >= 300: player_rect.bottom = 300 # "Colisão" com o chão
        player_animation()
        screen.blit(player_surf, player_rect)

        # OBSTACLE MOVEMENT
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # COLLISION
        game_active = collisions(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        
        score_message = test_font.render(f"Your score: {score}", False, '#7cccb4')
        score_message_rect = score_message.get_rect(center = (400, 340))
        
        screen.blit(game_title, game_title_rect)
        
        if game_over:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(instruct_surf, instruct_rect)
    
    pygame.display.update() # Desenha todos os elementos e atualiza os quadros
    clock.tick(60) # Determina o número de quadros por segundo (Nesse caso, 60fps) 
    