from pygame.surface import Surface

from .constants import BACKGROUNDS, BLACK, CANVAS_SIZE


class Editor:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.canvas = Surface(CANVAS_SIZE)

        self.theme = "red"

    def run(self, dt: float) -> None:
        # clear whole screen
        self.screen.fill(BLACK)

        # clear canvas
        self.canvas.fill(BACKGROUNDS[self.theme])

        self.screen.blit(self.canvas, (0, 0))

