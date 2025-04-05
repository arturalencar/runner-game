from screen import Screen
from game import Game

class GameScreen(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.game = Game()
        
    def handle_events(self, events):
        self.game.run_events(events)
        
    def update(self):
        self.game.update()
        
    def draw(self):
        self.game.draw()