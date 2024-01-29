import asyncio
from random import randint

import pygame
from custom_sprite import CustomSprite
from hammer import Hammer
from pygame.sprite import Group, GroupSingle, spritecollide

from zombie import Zombie

pygame.init()
screen = pygame.display.set_mode((850, 478))
pygame.display.set_caption("Zombie")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

zombies = Group()
zombies_positions = [(440, 350), (280, 360), (580, 380), (430, 450), (140, 460), (650, 460)]
# for zp in zombies_positions:
#     zombies.add(Zombie(midbottom=zp))

player = GroupSingle()
player.add(Hammer())

# Timer
zombies_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombies_timer, 800)


def handle_collisions():
    head_hammer_rect = player.sprite.rect.copy()
    head_hammer_rect.width = head_hammer_rect.width / 2

    head_hammer_sprite = CustomSprite(head_hammer_rect)
    collied_zombies = spritecollide(head_hammer_sprite, zombies, False)
    if collied_zombies and pygame.mouse.get_pressed()[0]:
        collied_zombies[0].kill()


async def main():
    bg = pygame.image.load("assets/images/horror-background.jpg").convert()

    running = True
    dt = 0

    appear_count = 0
    count = 0

    while running:
        count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == zombies_timer:
                if appear_count == 0:
                    amount = randint(2, len(zombies_positions))
                    for _ in range(amount):
                        idx = randint(0, len(zombies_positions) - 1)
                        zombies.add(Zombie(midbottom=zombies_positions[idx]))

                elif appear_count == 2:
                    appear_count = -1
                    zombies.empty()

                appear_count += 1

        screen.blit(bg, [0, 0])

        zombies.draw(screen)
        zombies.update()

        player.draw(screen)
        player.update(pygame.mouse.get_pos())

        handle_collisions()

        # pygame.display.flip()
        pygame.display.update()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
