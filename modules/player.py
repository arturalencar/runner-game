import pygame

class Player(pygame.sprite.Sprite):
    """
    Classe Player representa o jogador no jogo.

    Métodos:
        __init__():
            Inicializa os atributos do jogador, incluindo imagens, posição, gravidade e som de pulo.
        player_input():
            Verifica a entrada do jogador (tecla espaço ou clique do mouse) para realizar o pulo.
        apply_gravity():
            Aplica a gravidade ao jogador, ajustando sua posição vertical.
        animation_state():
            Atualiza a imagem do jogador com base no estado (caminhando ou pulando).
        update():
            Atualiza o estado do jogador chamando os métodos de entrada, gravidade e animação.
    """
            
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pygame.image.load("images/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("images/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("images/player/jump.png").convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.2)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.MOUSEBUTTONDOWN]) and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: self.rect.bottom = 300 
        
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()