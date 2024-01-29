from pygame import Rect
from pygame.sprite import Sprite


class CustomSprite(Sprite):
    def __init__(self, rect: Rect) -> None:
        super().__init__()
        self.rect = rect
