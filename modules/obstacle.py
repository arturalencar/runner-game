import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.animation_index = 0
        self.image = None
        self.rect = None

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 5
        self.destroy()       