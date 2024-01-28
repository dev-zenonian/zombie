from pygame.sprite import Sprite, _Group


class Hammer(Sprite):
    def __init__(self, *groups: _Group) -> None:
        super().__init__(*groups)
