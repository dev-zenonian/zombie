import asyncio

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
for zp in zombies_positions:
    zombies.add(Zombie(midbottom=zp))

player = GroupSingle()
player.add(Hammer())


def handle_collisions():
    head_hammer_rect = player.sprite.rect.copy()
    head_hammer_rect.width = head_hammer_rect.width / 2

    head_hammer_sprite = CustomSprite(head_hammer_rect)
    collied_zombies = spritecollide(head_hammer_sprite, zombies, False)
    if collied_zombies and pygame.mouse.get_pressed()[0]:
        collied_zombies[0].kill()


async def main():
    running = True
    dt = 0

    bg = pygame.image.load("assets/images/horror-background.jpg").convert()

    count = 0
    while running:
        count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
