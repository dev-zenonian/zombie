from pygame import image, mouse, transform
from pygame.sprite import Sprite


class Hammer(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.origin_image = image.load("assets/images/hammer.png")
        self.image = transform.rotozoom(self.origin_image, 0, 0.22)
        self.rect = self.image.get_rect()

        self.rotate_value = -30
        self.is_pressed = False

    def hit(self):
        self.image = transform.rotozoom(self.origin_image, self.rotate_value, 0.22)

    def check_pressed(self):
        self.is_pressed = mouse.get_pressed()[0]

    def handle_press(self):
        if not self.is_pressed:
            self.check_pressed()
        if self.is_pressed:
            if self.rotate_value < 30:
                self.rotate_value += 10
            else:
                self.rotate_value = -30
                self.is_pressed = False
            self.hit()

    def update_pos(self, pos: tuple[int, int]):
        x, y = pos
        self.rect.x = x - int(self.rect.width / 2)
        self.rect.y = y - int(self.rect.height / 2)

    def update(self, pos: tuple[int, int]):
        self.update_pos(pos)
        self.handle_press()
