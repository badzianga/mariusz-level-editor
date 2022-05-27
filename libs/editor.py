from pygame.surface import Surface

from .constants import BLACK

class Editor:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen

    def run(self, dt: float) -> None:
        self.screen.fill(BLACK)