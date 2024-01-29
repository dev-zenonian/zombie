from enum import Enum

from pygame import SRCALPHA, Surface
from pygame.font import Font
from pygame.sprite import Sprite


class CollisionState(Enum):
    HIT = 5
    MISS = -10
    NONE = 0


class ScoreBoard(Sprite):
    def __init__(self) -> None:
        super().__init__()

        font_path = "assets/fonts/halloween.otf"
        self.h1 = Font(font_path, 36)
        self.p = Font(font_path, 24)

        self.hit = 0
        self.miss = 0
        self.score = 0

        game_title = self.h1.render("Hello Zombie", False, (111, 196, 169))
        score_title = self.p.render(
            f"Score - hit: {self.hit}, miss: {self.miss} ", False, (111, 196, 169)
        )
        self.image = Surface(
            (score_title.get_width(), game_title.get_height() + 10 + score_title.get_height()),
            SRCALPHA,
        )

        self.image.blit(game_title, ((0, 0)))
        self.image.blit(score_title, ((0, game_title.get_height() + 10)))
        self.rect = self.image.get_rect()

    def reset(self):
        self.hit = 0
        self.miss = 0
        self.score = 0

    def update(self, state: CollisionState):
        if state == CollisionState.HIT:
            self.hit += 1
        elif state == CollisionState.MISS:
            self.miss += 1

        self.score += state.value

        game_title = self.h1.render("Hello Zombie", False, (111, 196, 169))
        score_title = self.p.render(
            f"Score: {self.score} -- hit: {self.hit}, miss: {self.miss} ", False, (111, 196, 169)
        )
        self.image = Surface(
            (score_title.get_width(), game_title.get_height() + 10 + score_title.get_height()),
            SRCALPHA,
        )
        self.image.blit(game_title, ((0, 0)))
        self.image.blit(score_title, ((0, game_title.get_height() + 10)))
        self.rect = self.image.get_rect()
