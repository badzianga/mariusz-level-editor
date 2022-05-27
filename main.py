from sys import exit
from time import time

from pygame import init, quit
from pygame.constants import K_ESCAPE, K_F11, K_F12, KEYDOWN, QUIT
from pygame.display import set_caption, set_icon, set_mode
from pygame.display import update as update_display
from pygame.event import get as get_events
from pygame.image import load as load_image
from pygame.surface import Surface
from pygame.time import Clock
from pygame.transform import scale

from libs.constants import DISPLAY_SIZE, FPS, SCREEN_SIZE
from libs.debug import Debug
from libs.editor import Editor


def main() -> None:
    init()

    screen = set_mode(SCREEN_SIZE)
    clock = Clock()

    set_caption("Mariusz Level Edutor")
    set_icon(load_image("icon.png").convert_alpha())

    display = Surface(DISPLAY_SIZE)
    editor = Editor(display)
    debug = Debug(display, clock)
    last_time = time()

    while True:
        dt = (time() - last_time) * FPS
        last_time = time()

        for event in get_events():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif event.key == K_F11:
                    editor.toggle_grid()
                elif event.key == K_F12:
                    debug.toggle_fps()

        editor.update(dt)
        editor.draw()

        debug.draw()

        screen.blit(scale(display, SCREEN_SIZE), (0, 0))
        update_display()
        clock.tick()


if __name__ == '__main__':
    main()

    quit()
    exit()
    