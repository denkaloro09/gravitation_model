import pygame

import button
import planet_storage
import planets
from random import randint

W = 1000
H = 700

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60
pygame.init()

sc = pygame.display.set_mode((W, H))

#  поверхность для траектории (следа)
plt_sc = pygame.Surface((W, H))
sc.blit(plt_sc, (0, 0))

#  счетчик планет
font = pygame.font.SysFont('arial', 20)
count_sc = font.render('', True, WHITE)
counter_pos = count_sc.get_rect(center=(W-30, 30))

# хранилище планет
stg = planet_storage.Storage()
stg.add_obj(planets.Planet(W // 2, 70, GREEN, 1000, 10, (11, 0), False))
stg.add_obj(planets.Planet(W // 2, 200, RED, 2000, 17, (15, 0), False))
stg.add_obj(planets.Planet(W // 2, H // 2, YELLOW, 35000, 30, (0, 0), True))


# кнопки управления
trace_btn = button.Button('Clean trace', (W-100, 60), WHITE)

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and trace_btn.pressed(event.pos):
            plt_sc.fill(BLACK)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()  # обнуляем смещение
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            rel = pygame.mouse.get_rel()
            rand_clr = (randint(0, 255), randint(0, 255), randint(0, 255))
            stg.add_obj(planets.Planet(event.pos[0], event.pos[1], rand_clr, 100, 5, (rel[0]//5, rel[1]//5), False))

    pressed = pygame.mouse.get_pressed()
    if stg.is_planets_collide_point(pygame.mouse.get_pos()):
        if pressed[0] and stg.is_planets_collide_point(pygame.mouse.get_pos()):
            rel = pygame.mouse.get_rel()
            stg.move_by_mouse(rel)
            stg.draw(sc, plt_sc)
        else:
            stg.cancel_planet_clicks()

    count_sc = font.render(f'{stg.count()}', True, WHITE)

    sc.fill(BLACK)

    stg.simulate_moving()
    sc.blit(plt_sc, (0, 0))
    sc.blit(count_sc, counter_pos)
    trace_btn.blit_bt(sc)
    stg.draw(sc, plt_sc)
    pygame.display.update()
    clock.tick(FPS)
