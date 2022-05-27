from pygame.constants import K_LEFT, K_LSHIFT, K_RIGHT, K_RSHIFT
from pygame.draw import line as draw_line
from pygame.key import get_pressed
from pygame.surface import Surface

from .constants import (BACKGROUNDS, CANVAS_SIZE, GRAY, MAP_SIZE, MAX_SCROLL,
                        SCROLL, SCROLL_MULT, TILE_SIZE, WHITE)


class Editor:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.canvas = Surface(CANVAS_SIZE)

        self.theme = "red"

        self.x_scroll = 0

        self.show_grid = True

    def draw_grid(self) -> None:
        if not self.show_grid:
            return
        # vertical lines
        for x in range(1, MAP_SIZE[0]):
            draw_line(
                self.canvas, WHITE,
                (x * TILE_SIZE - self.x_scroll, 0),
                (x * TILE_SIZE - self.x_scroll, CANVAS_SIZE[1])
            )
        # horizontal lines
        for y in range(1, MAP_SIZE[1]):
            draw_line(
                self.canvas, WHITE,
                (0, y * TILE_SIZE),
                (CANVAS_SIZE[0], y * TILE_SIZE)
            )

    def draw(self) -> None:
        # clear whole screen
        self.screen.fill(GRAY)

        # clear canvas
        self.canvas.fill(BACKGROUNDS[self.theme])

        self.draw_grid()

        self.screen.blit(self.canvas, (0, 0))

    def update(self, dt: float) -> None:
        keys = get_pressed()
        mult = 1

        if keys[K_LSHIFT] or keys[K_RSHIFT]:
            mult = SCROLL_MULT
        if keys[K_LEFT]:
            self.x_scroll = max(self.x_scroll - SCROLL * mult * dt, 0)
        if keys[K_RIGHT]:
            self.x_scroll = min(self.x_scroll + SCROLL * mult * dt, MAX_SCROLL)
        
        self.draw()

    def toggle_grid(self) -> None:
        self.show_grid = not self.show_grid

