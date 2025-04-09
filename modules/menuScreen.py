from modules.screen import Screen
import pygame, sys

class MenuScreen(Screen):
    """
    Classe que representa a tela de menu do jogo.            
    """
    def __init__(self, screen):
        """
        Inicializa a tela de menu, configurando fontes, textos, botões e imagens.
        """
        super().__init__(screen)
        self.font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.title = self.font.render("Pixel Runner", True, "#7cccb4")
        self.title_rect = self.title.get_rect(center=(400, 50))
        
        self.play_button_rect = pygame.Rect(190, 300, 200, 50)
        self.play_text = self.font.render("Play", True, '#457b9d')
        self.play_text_rect = self.play_text.get_rect(center=(290,330))
        
        self.quit_button_rect = pygame.Rect(410, 300, 200, 50)
        self.quit_text = self.font.render("Quit", True, '#457b9d')
        self.quit_text_rect = self.quit_text.get_rect(center=(510, 330))
        
        self.hand_cursor = False
        
        self.player_stand = pygame.image.load("images/player/player_stand.png").convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center=(400, 180))
        
    def handle_events(self, events):
        """
        Lida com os eventos do mouse, alterando o cursor e navegando para outras telas ou encerrando o jogo.
        """
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.play_button_rect.collidepoint(event.pos) or self.quit_button_rect.collidepoint(event.pos):
                    if not self.hand_cursor:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        self.hand_cursor = True
                else:
                    if self.hand_cursor:
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  
                        self.hand_cursor = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button_rect.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  
                    return "game"
                elif self.quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    
    def draw(self):
        """
        Desenha os elementos da tela de menu, incluindo o título, botões e imagem do jogador.
        """
        self.screen.fill((94, 129, 162))
        self.screen.blit(self.title, self.title_rect)
        pygame.draw.rect(self.screen, "#caf0f8", self.play_button_rect)
        pygame.draw.rect(self.screen, "#caf0f8", self.quit_button_rect)
        self.screen.blit(self.play_text, self.play_text_rect)
        self.screen.blit(self.quit_text, self.quit_text_rect)
        self.screen.blit(self.player_stand, self.player_stand_rect)
