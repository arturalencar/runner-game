import pygame, sys

pygame.init() #Inicia o pygame

screen = pygame.display.set_mode(size=(800,400)) # Cria a janela do jogo (width, height)
pygame.display.set_caption("Runner") # Define o título da janela
clock = pygame.time.Clock() # Cria um objeto de clock
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

# Cria novas superfícies
sky_surface = pygame.image.load("./images/Sky.png").convert()
ground_surface = pygame.image.load("./images/ground.png").convert()

score_surf = test_font.render("Runner Game", False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela do pygame (o programa continua rodando)
            sys.exit() # Encerra o programa
        
        # 1º Verificar o clique 
        # 2º Verificar colisão
        # Desse modo, é mais eficiente do que o inverso
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
                snail_rect.left = 800
            

    if game_active:
        screen.blit(sky_surface,(0,0)) # Desenha a superfície na tela
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect) # Desenha a forma na tela
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(score_surf, score_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800 # Reseta a posição do caracol quando ele sai da tela
        screen.blit(snail_surf, snail_rect)
        
        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity # Movimento de queda
        if player_rect.bottom >= 300: player_rect.bottom = 300 # "Colisão" com o chão
        screen.blit(player_surf, player_rect)

        # COLLISION
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('blue')
    
    pygame.display.update() # Desenha todos os elementos e atualiza os quadros
    clock.tick(60) # Determina o número de quadros por segundo (Nesse caso, 60fps) 
    