from modules.screen import Screen
from modules.game import Game

class GameScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.game = Game()
        
    def handle_events(self, events):
        self.game.run_events(events)
        if self.game.game_over:
            return "game_over"
        
    def update(self):
        self.game.update()
        
        
    def draw(self):
        self.game.draw()