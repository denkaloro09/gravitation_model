import pygame

import planet_storage
import planets


W = 1000
H = 700
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 60
pygame.init()
sc = pygame.display.set_mode((W, H))
plt_sc = pygame.Surface((W, H))
sc.blit(plt_sc, (0, 0))

stg = planet_storage.Storage()
stg.add_obj(planets.Planet(W//2, H//2, YELLOW, 35000, 20, 0, 0, False))
stg.add_obj(planets.Planet(W//2, 100, GREEN, 20, 3, 10, 0, False))
stg.add_obj(planets.Planet(W//3, 100, RED, 50, 5, 5, 0, False))
stg.draw(sc, plt_sc)
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)
    stg.simulate_moving()
    sc.blit(plt_sc, (0, 0))
    stg.draw(sc, plt_sc)
    pygame.display.update()
    clock.tick(FPS)
