from pygame.mouse import get_pos as get_mouse_pos
from pygame.surface import Surface


class Button():
    def __init__(self, position: tuple, image: Surface) -> None:
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, self.rect)

    def check_pressed(self) -> bool:
        if self.rect.collidepoint(get_mouse_pos()):
            return True
        return False
