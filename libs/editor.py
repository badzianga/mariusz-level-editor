from pygame.surface import Surface
from pygame.draw import line as draw_line

from .constants import BACKGROUNDS, CANVAS_SIZE, GRAY, MAP_SIZE, WHITE


class Editor:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.canvas = Surface(CANVAS_SIZE)

        self.theme = "red"

        self.show_grid = True

    def draw_grid(self) -> None:
        if not self.show_grid:
            return
        for x in range(1, MAP_SIZE[0]):
            draw_line(
                self.canvas, WHITE, (x * 16, 0), (x * 16, CANVAS_SIZE[1])
            )
        for y in range(1, MAP_SIZE[1]):
            draw_line(
                self.canvas, WHITE, (0, y * 16), (CANVAS_SIZE[0], y * 16)
            )

    def run(self, dt: float) -> None:
        # clear whole screen
        self.screen.fill(GRAY)

        # clear canvas
        self.canvas.fill(BACKGROUNDS[self.theme])

        self.draw_grid()

        self.screen.blit(self.canvas, (0, 0))

    def toggle_grid(self) -> None:
        self.show_grid = not self.show_grid