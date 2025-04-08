import pygame, sys
from screenManager import ScreenManager

def main():
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