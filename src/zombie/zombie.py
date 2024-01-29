from pygame import image, transform
from pygame.sprite import Sprite


class Zombie(Sprite):
    def __init__(self, midbottom: tuple[int, int]) -> None:
        super().__init__()
        self.origin_image = image.load("assets/images/zombie.png").convert_alpha()
        self.origin_image = transform.rotozoom(self.origin_image, 0, 0.2)
        self.origin_rect = self.origin_image.get_rect()
        self.origin_height = self.origin_rect.height

        self.dynamic_rect = self.origin_rect.copy()
        self.dynamic_rect.height = 0
        self.image = self.origin_image.subsurface(self.dynamic_rect)

        self.rect = self.image.get_rect(midbottom=midbottom)  # remember to keep rect to render
        self.origin_y = self.rect.y

    def up(self):
        pad = self.origin_y - self.rect.y
        if pad < self.origin_height:
            remain = self.origin_height - pad
            change = 6 if remain > 6 else remain
            self.rect.y -= change
            self.rect.height += change  # actual height for the surface
            self.dynamic_rect.height += change
            self.image = self.origin_image.subsurface(
                self.dynamic_rect
            )  # use sub surface to cut correct height from original image

    def update(self):
        self.up()
