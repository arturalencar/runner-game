class Screen:
    """
    Classe Screen para gerenciar a tela do jogo.
    Atributos:
        screen: Objeto que representa a tela do jogo.
    Métodos:
        handle_events(events):
            Deverá ser implementada nas subclasses para lidar com os eventos recebidos pela tela.
        update():
            Deverá ser implementada nas subclasses atualizar os elementos e o estado da tela.
        draw():
            Deverá ser implementada nas subclasses desenhar os elementos na tela.
    """
    def __init__(self, screen):
        self.screen = screen
        
    def handle_events(self, events):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
        