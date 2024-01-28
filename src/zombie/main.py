import asyncio

import pygame
from pygame.sprite import Group

from zombie import Zombie

pygame.init()
screen = pygame.display.set_mode((850, 478))
pygame.display.set_caption("Zombie")
clock = pygame.time.Clock()

zombies = Group()
zombies_positions = [(440, 350), (280, 360), (580, 380), (430, 450), (140, 460), (650, 460)]
for zp in zombies_positions:
    zombies.add(Zombie(midbottom=zp))


async def main():
    running = True
    dt = 0

    bg = pygame.image.load("assets/images/horror-background.jpg").convert()

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    count = 0
    while running:
        count += 1
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(bg, [0, 0])
        # screen.blit(zombie, player_pos)
        zombies.draw(screen)

        # pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()
        zombies.update()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
