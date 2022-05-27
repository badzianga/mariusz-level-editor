from numpy import loadtxt, savetxt, uint8, zeros
from pygame.constants import K_LEFT, K_LSHIFT, K_RIGHT, K_RSHIFT
from pygame.draw import line as draw_line
from pygame.draw import rect as draw_rect
from pygame.key import get_pressed as get_pressed_keys
from pygame.mouse import get_pressed as get_pressed_mouse
from pygame.surface import Surface

from .constants import (BACKGROUNDS, CANVAS_SIZE, GRAY, MAP_SIZE, MAX_SCROLL,
                        RED, SCROLL, SCROLL_MULT, TILE_SIZE, WHITE)


class Editor:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.canvas = Surface(CANVAS_SIZE)

        self.theme = "red"

        self.x_scroll = 0
        self.current_tile = 1
        self.map_data = zeros((MAP_SIZE[1], MAP_SIZE[0]), uint8)
        self.tile_buttons = {}

        self.show_grid = True

    def draw_grid(self) -> None:
        """Draw helping grid."""
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

    def draw_buttons(self) -> None:
        "Draw all buttons and highlight selected tile."
        for button in self.tile_buttons:
            button.draw()
        # draw_rect(self.screen, RED, self.tile_buttons[self.current_tile], 1)

    def draw(self) -> None:
        """Draw interface od the editor."""
        # clear whole screen
        self.screen.fill(GRAY)

        # clear canvas
        self.canvas.fill(BACKGROUNDS[self.theme])

        self.draw_grid()
        self.draw_buttons()
        self.screen.blit(self.canvas, (0, 0))

    def update(self, dt: float) -> None:
        """Get inputs from player and scroll map."""
        keys = get_pressed_keys()
        mult = 1

        if keys[K_LSHIFT] or keys[K_RSHIFT]:
            mult = SCROLL_MULT
        if keys[K_LEFT]:
            self.x_scroll = max(self.x_scroll - SCROLL * mult * dt, 0)
        if keys[K_RIGHT]:
            self.x_scroll = min(self.x_scroll + SCROLL * mult * dt, MAX_SCROLL)

        if get_pressed_mouse()[0]:
            for button in self.tile_buttons:
                if button.check_pressed():
                    self.current_tile = button.id
                    break

    def toggle_grid(self) -> None:
        """Toggle visibility of grid."""
        self.show_grid = not self.show_grid

