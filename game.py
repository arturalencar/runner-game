import pygame, sys
from random import choice
from player import Player
from fly import Fly
from snail import Snail

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(800, 400))
        pygame.display.set_caption("Runner")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)
        #self.game_active = False
        self.start_time = 0
        self.score = 0
        self.game_over = False
        
        # Background music
        self.bg_music = pygame.mixer.Sound('audio/music.wav')
        self.bg_music.play(loops=-1)
        self.bg_music.set_volume(0.3)

        # Groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.obstacle_group = pygame.sprite.Group()

        # Surfaces
        self.sky_surface = pygame.image.load("./images/Sky.png").convert()
        self.ground_surface = pygame.image.load("./images/ground.png").convert()

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def display_score(self):
        current_time = int((pygame.time.get_ticks() - self.start_time) / 1000)
        score_surf = self.font.render(f'Score:  {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        self.screen.blit(score_surf, score_rect)
        return current_time

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            return True
        return False

    def reset_game(self):
        """ Reinicia o estado do jogo """
        
        self.start_time = pygame.time.get_ticks()
        self.score = 0
        self.game_over = False
        self.obstacle_group.empty()
        self.player.sprite.rect.midbottom = (80, 300)
        self.player.sprite.gravity = 0
        

    def run_events(self, events):
        for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not self.game_over:
                    if event.type == self.obstacle_timer:
                        obstacle_type = choice(['fly', 'snail', 'snail', 'snail', 'fly'])
                        if obstacle_type == 'fly':
                            self.obstacle_group.add(Fly())
                        else:
                            self.obstacle_group.add(Snail())

    def update(self):
        self.player.update()
        self.obstacle_group.update()
        self.game_over = self.collision_sprite()
    
    def draw(self):
        if not self.game_over:
            self.screen.blit(self.sky_surface, (0, 0))
            self.screen.blit(self.ground_surface, (0, 300))
            self.score = self.display_score()

            self.player.draw(self.screen)

            self.obstacle_group.draw(self.screen)