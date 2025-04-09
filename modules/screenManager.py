from modules.menuScreen import MenuScreen
from modules.gameScreen import GameScreen
from modules.gameOverScreen import GameOverScreen

class ScreenManager: 
    """
    Gerencia as diferentes telas do jogo, incluindo transições entre elas, atualização de lógica e renderização.
    
    Atributos:
        screen (pygame.Surface): Superfície de exibição onde as telas serão desenhadas.
        screens (dict): Dicionário contendo as instâncias das telas do jogo.
        current_screen (str): Nome da tela atualmente ativa.
    
    Métodos:
        __init__(screen):
            Inicializa o ScreenManager com a superfície de exibição e configura as telas disponíveis.
        handle_events(events):
            Trata os eventos de entrada delegando-os para a tela atual. 
            Alterna para uma nova tela caso a tela atual retorne o nome de outra tela.
        update():
            Atualiza a lógica da tela atualmente ativa.
        draw():
            Renderiza a tela atualmente ativa na superfície de exibição.
    """
    
    def __init__(self, screen):        
        self.screen = screen
        self.screens = {
            "menu": MenuScreen(screen),
            "game": GameScreen(screen),
            "game_over": None
        }
        self.current_screen = "menu"
        
    def handle_events(self, events):
        next_screen = self.screens[self.current_screen].handle_events(events)
        
        if next_screen in self.screens:
            if next_screen == "game_over":
                game_screen = self.screens["game"]
                self.screens["game_over"] = GameOverScreen(self.screen, game_screen.game.score)
                
            if next_screen == "game" :
                self.screens["game"].game.reset_game()
                
            self.current_screen = next_screen
            
    def update(self):
        self.screens[self.current_screen].update()
        
    def draw(self):
        self.screens[self.current_screen].draw()
        
