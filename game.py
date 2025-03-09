import pygame, sys

pygame.init() #Inicia o pygame

screen = pygame.display.set_mode(size=(800,400)) # Cria a janela do jogo (width, height)
pygame.display.set_caption("Runner") # Define o título da janela
clock = pygame.time.Clock() # Cria um objeto de clock
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)


# Cria novas superfícies preenchidas por imagens
sky_surface = pygame.image.load("./images/Sky.png").convert()
ground_surface = pygame.image.load("./images/ground.png").convert()

text_surface = test_font.render("Runner Game", False, "black")

snail_surf = pygame.image.load("images/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha a janela do pygame (o programa continua rodando)
            sys.exit() # Encerra o programa
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    
    pygame.display.update() # Desenha todos os elementos e atualiza os quadros
    clock.tick(60) # Determina o número de quadros por segundo (Nesse caso, 60fps) 
    