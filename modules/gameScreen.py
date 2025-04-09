from modules.screen import Screen
from modules.game import Game

class GameScreen(Screen):
    def __init__(self, screen):
        """
        Inicializa a tela do jogo e cria uma instância do jogo.
        """
        super().__init__(screen)
        self.game = Game()
        
    def handle_events(self, events):
        """
        Lida com os eventos recebidos e verifica se o jogo terminou.
        """
        self.game.run_events(events)
        if self.game.game_over:
            return "game_over"
        
    def update(self):
        """
        Atualiza o estado do jogo.
        """
        self.game.update()
        
        
    def draw(self):
        """
        Desenha os elementos do jogo na tela.
        """
        self.game.draw()