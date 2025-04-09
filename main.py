import pygame, sys
from modules.screenManager import ScreenManager

def main():
    """
    Função principal do jogo Runner.
    - Inicializa o módulo pygame e configura a janela do jogo.
    - Define o título da janela e a taxa de atualização (FPS).
    - Cria uma instância de ScreenManager para gerenciar as telas do jogo.
    - Loop principal:
        - Captura e processa eventos do pygame.
        - Encerra o jogo ao detectar o evento QUIT.
        - Delega o tratamento de eventos, atualização e desenho para o ScreenManager.
        - Atualiza a tela e controla a taxa de quadros por segundo.
    """
    
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Runner")
    clock = pygame.time.Clock()
    
    screen_manager = ScreenManager(screen)
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen_manager.handle_events(events)
        screen_manager.update()
        screen_manager.draw()
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    main()