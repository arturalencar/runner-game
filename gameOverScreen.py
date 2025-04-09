from screen import Screen
import pygame

class GameOverScreen(Screen):
    def __init__(self, screen, score):
        super().__init__(screen)
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.title = self.font.render("Game Over", True, "#e63946")
        self.title_rect = self.title.get_rect(center=(400, 100))
        
        self.score_text = self.font.render(f"Your score: {score}", False, '#7cccb4')
        self.score_text_rect = self.score_text.get_rect(center=(400, 200))
        
        self.retry_button_rect = pygame.Rect(190, 300, 200, 50)
        self.retry_text = self.font.render("Retry", True, '#457b9d')
        self.retry_text_rect = self.retry_text.get_rect(center=(290, 330))

        self.back_button_rect = pygame.Rect(410, 300, 200, 50)
        self.back_text = self.font.render("Back", True, '#457b9d')
        self.back_text_rect = self.back_text.get_rect(center=(510, 330))

        self.hand_cursor = False

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.retry_button_rect.collidepoint(event.pos) or self.back_button_rect.collidepoint(event.pos):
                    if not self.hand_cursor:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        self.hand_cursor = True
                else:
                    if self.hand_cursor:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        self.hand_cursor = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.retry_button_rect.collidepoint(event.pos):
                    return "game"  # Reinicia o jogo
                elif self.back_button_rect.collidepoint(event.pos):
                    return "menu"

    def draw(self):
        self.screen.fill((94, 129, 162))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.score_text, self.score_text_rect)
        pygame.draw.rect(self.screen, "#caf0f8", self.retry_button_rect)
        pygame.draw.rect(self.screen, "#caf0f8", self.back_button_rect)
        self.screen.blit(self.retry_text, self.retry_text_rect)
        self.screen.blit(self.back_text, self.back_text_rect)