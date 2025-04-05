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
        self.test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.game_active = False
        self.start_time = 0
        self.score = 0
        self.game_over = False

        # Background music
        self.bg_music = pygame.mixer.Sound('audio/music.wav')
        self.bg_music.play(loops=-1)
        self.bg_music.set_volume(0.4)

        # Groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.obstacle_group = pygame.sprite.Group()

        # Surfaces
        self.sky_surface = pygame.image.load("./images/Sky.png").convert()
        self.ground_surface = pygame.image.load("./images/ground.png").convert()

        # Intro screen
        self.player_stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center=(400, 200))

        self.game_title = self.test_font.render("Pixel Runner", False, '#7cccb4')
        self.game_title_rect = self.game_title.get_rect(center=(400, 70))

        self.instruct_surf = self.test_font.render("Press SPACE to run", False, '#7cccb4')
        self.instruct_rect = self.instruct_surf.get_rect(center=(400, 340))

        self.score_message = self.test_font.render(f"Your score: {self.score}", False, '#7cccb4')
        self.score_message_rect = self.score_message.get_rect(center=(400, 340))

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def display_score(self):
        current_time = int((pygame.time.get_ticks() - self.start_time) / 1000)
        score_surf = self.test_font.render(f'Score:  {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        self.screen.blit(score_surf, score_rect)
        return current_time

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            self.game_over = True
            return False
        return True

    def run(self):
        while True:
            # EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.game_active:
                    if event.type == self.obstacle_timer:
                        obstacle_type = choice(['fly', 'snail', 'snail', 'snail'])
                        if obstacle_type == 'fly':
                            self.obstacle_group.add(Fly())
                        else:
                            self.obstacle_group.add(Snail())
                        # self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_active = True
                        self.start_time = pygame.time.get_ticks()

            # STATES
            if self.game_active:
                self.screen.blit(self.sky_surface, (0, 0))
                self.screen.blit(self.ground_surface, (0, 300))
                self.score = self.display_score()

                self.player.draw(self.screen)
                self.player.update()

                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()

                # COLLISION
                self.game_active = self.collision_sprite()

            else:
                self.screen.fill((94, 129, 162))
                self.screen.blit(self.player_stand, self.player_stand_rect)

                self.score_message = self.test_font.render(f"Your score: {self.score}", False, '#7cccb4')
                self.score_message_rect = self.score_message.get_rect(center=(400, 340))
                self.screen.blit(self.game_title, self.game_title_rect)

                if self.game_over:
                    self.screen.blit(self.score_message, self.score_message_rect)
                    
                else:
                    self.screen.blit(self.instruct_surf, self.instruct_rect)

            pygame.display.update()
            self.clock.tick(60)

# Inicializa o jogo
if __name__ == "__main__":
    game = Game()
    game.run()