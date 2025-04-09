from modules.obstacle import Obstacle
import pygame
from random import randint

class Snail(Obstacle):
    """
    Representa um obstáculo do tipo caracol no jogo.

    Métodos:
        __init__:
            Inicializa o objeto Snail, carregando as imagens de animação,
            configurando os quadros e definindo a posição inicial do caracol.
    """
    def __init__(self):
        super().__init__()
        snail_1 = pygame.image.load("images/snail/snail1.png").convert_alpha()
        snail_2 = pygame.image.load("images/snail/snail2.png").convert_alpha()
        self.frames = [snail_1, snail_2]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 300))