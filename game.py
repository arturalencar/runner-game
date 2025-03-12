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
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
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

# Cria novas superfícies
sky_surface = pygame.image.load("./images/Sky.png").convert()
ground_surface = pygame.image.load("./images/ground.png").convert()

# OBSTACLES
snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
fly_surf = pygame.image.load("images/fly/Fly1.png").convert_alpha()

obstacle_rect_list = []



player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
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
pygame.time.set_timer(obstacle_timer, 900)

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
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
                
    # STATES
    if game_active:
        screen.blit(sky_surface,(0,0)) # Desenha a superfície na tela
        screen.blit(ground_surface,(0,300))
        score = display_score()
        

        
        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity # Movimento de queda
        if player_rect.bottom >= 300: player_rect.bottom = 300 # "Colisão" com o chão
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
    