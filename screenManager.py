from menuScreen import MenuScreen
from gameScreen import GameScreen

"""
    Gerencia múltiplas telas em um jogo ou aplicação, permitindo alternar
    entre diferentes telas (ex.: menu, jogo) e delegando o tratamento de eventos,
    atualizações e desenhos para a tela ativa.
    
    Atributos:
        screen: A superfície principal de exibição onde todas as telas serão renderizadas.
        screens: Um dicionário que mapeia os nomes das telas para seus respectivos objetos.
        current_screen: O nome da tela atualmente ativa.
"""

class ScreenManager:
    def __init__(self, screen):
        """
        Inicializa o ScreenManager com uma superfície de exibição e configura as telas
        """
        
        self.screen = screen
        self.screens = {
            "menu": MenuScreen(screen),
            "game": GameScreen(screen)
        }
        self.current_screen = "menu"
        
    def handle_events(self, events):
        """
        Trata os eventos de entrada delegando-os para a tela atual. Se a tela atual retornar o nome de uma nova tela, alterna para essa tela.
        """
        
        next_screen = self.screens[self.current_screen].handle_events(events)
        
        if next_screen:
            self.current_screen = next_screen
            
    def update(self):
        """
        Atualiza a lógica da tela atual.
        """
        self.screens[self.current_screen].update()
        
    def draw(self):
        """
        Desenha a tela atual na superfície de exibição.
        """
        self.screens[self.current_screen].draw()
        
