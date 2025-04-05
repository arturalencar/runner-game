from screen import Screen
import pygame
import sys

class MenuScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.title = self.font.render("Pixel Runner", True, "#7cccb4")
        self.title_rect = self.title.get_rect(center=(400, 100))
        
        self.start_button = self.font.render("Play", True, "#FFFFFF")
        self.start_button_rect = self.start_button.get_rect(center=(400,200))
        
        self.ctrl_button = self.font.render("Controls", True, "#ffffff")
        self.ctrl_button_rect = self.ctrl_button.get_rect(center=(400, 290))
        
        self.quit_button = self.font.render("Quit", True, "#ffffff")
        self.quit_button_rect = self.quit_button.get_rect(center=(400, 380))
        
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    return "game"
                elif self.ctrl_button_rect.collidepoint(event.pos):
                    return "controls"
                elif self.quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    
    def draw(self):
        self.screen.fill((94, 129, 162))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.start_button, self.start_button_rect)
        self.screen.blit(self.ctrl_button, self.ctrl_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)