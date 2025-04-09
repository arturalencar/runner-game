from modules.obstacle import Obstacle
import pygame
from random import randint

class Fly(Obstacle):
    """
    Representa um obstáculo do tipo 'Fly' no jogo.

    Métodos:
        __init__:
            Inicializa a classe Fly, carregando as imagens de animação e definindo a posição inicial do obstáculo.
    """
    def __init__(self):
        super().__init__()
        fly_1 = pygame.image.load("images/fly/Fly1.png").convert_alpha()
        fly_2 = pygame.image.load("images/fly/Fly2.png").convert_alpha()
        self.frames = [fly_1, fly_2]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), 210))
