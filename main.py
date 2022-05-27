from sys import exit
from time import time

from pygame import init, quit
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT
from pygame.display import set_caption, set_icon, set_mode
from pygame.display import update as update_display
from pygame.event import get as get_events
from pygame.image import load as load_image
from pygame.surface import Surface
from pygame.time import Clock
from pygame.transform import scale

from libs.constants import DISPLAY_SIZE, FPS, SCREEN_SIZE
from libs.editor import Editor


def main() -> None:
    init()

    screen = set_mode(SCREEN_SIZE)
    clock = Clock()

    set_caption("Mariusz Level Edutor")
    set_icon(load_image("icon.png").convert_alpha())

    display = Surface(DISPLAY_SIZE)
    editor = Editor(display)
    last_time = time()

    while True:
        dt = (time() - last_time) * FPS
        last_time = time()

        editor.run(dt)

        for event in get_events():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        screen.blit(scale(display, SCREEN_SIZE), (0, 0))
        update_display()
        clock.tick()


if __name__ == '__main__':
    main()

    quit()
    exit()
    