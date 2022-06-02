import pygame

import planet_storage
import planets

W = 1000
H = 700

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()
FPS = 30
pygame.init()

sc = pygame.display.set_mode((W, H))
#  поверхность для траектории (следа)
plt_sc = pygame.Surface((W, H))
sc.blit(plt_sc, (0, 0))

font = pygame.font.SysFont('arial', 20)
count_sc = font.render('', 1, WHITE)
counter_pos = count_sc.get_rect(center=(W-30, 30))

stg = planet_storage.Storage()

stg.add_obj(planets.Planet(W // 2, 100, GREEN, 500, 10, (10, 0), False))
stg.add_obj(planets.Planet(W // 2, 200, RED, 1000, 17, (15, 0), False))
stg.add_obj(planets.Planet(W // 2, H // 2, YELLOW, 30000, 30, (0, 0), True))

stg.draw(sc, plt_sc)
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()  # обнуляем смещение
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            rel = pygame.mouse.get_rel()
            stg.add_obj(planets.Planet(event.pos[0], event.pos[1], BLUE, 100, 5, (rel[0]//5,rel[1]//5), False))

    pressed = pygame.mouse.get_pressed()
    if stg.is_planets_collide_point(pygame.mouse.get_pos()):
        if pressed[0] and stg.is_planets_collide_point(pygame.mouse.get_pos()):
            rel = pygame.mouse.get_rel()
            stg.move_by_mouse(rel)
            stg.draw(sc, plt_sc)
        else:
            stg.cancel_planet_clicks()

    count_sc = font.render(f'{stg.count()}', 1, WHITE)

    sc.fill(BLACK)

    stg.simulate_moving()
    sc.blit(plt_sc, (0, 0))
    sc.blit(count_sc, counter_pos)
    stg.draw(sc, plt_sc)
    pygame.display.update()
    clock.tick(FPS)
