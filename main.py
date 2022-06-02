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
FPS = 30
pygame.init()
sc = pygame.display.set_mode((W, H))
plt_sc = pygame.Surface((W, H))
sc.blit(plt_sc, (0, 0))

stg = planet_storage.Storage()
stg.add_obj(planets.Planet(W//2, H//2, YELLOW, 35000, 30, 0, 0, True))
stg.add_obj(planets.Planet(W//2, 100, GREEN, 20, 8, 10, 0, False))
stg.add_obj(planets.Planet(W//3, 100, RED, 50, 15, 5, 0, False))
stg.draw(sc, plt_sc)
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    pressed = pygame.mouse.get_pressed()
    if stg.is_planets_collide_point(pygame.mouse.get_pos()):
        if pressed[0] and stg.is_planets_collide_point(pygame.mouse.get_pos()):
            rel = pygame.mouse.get_rel()
            stg.move_by_mouse(rel)
            stg.draw(sc, plt_sc)
        else:
            stg.cancel_planet_clicks()

    sc.fill(BLACK)
    stg.simulate_moving()
    sc.blit(plt_sc, (0, 0))
    stg.draw(sc, plt_sc)
    pygame.display.update()
    clock.tick(FPS)
