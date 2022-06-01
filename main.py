import pygame
import planets

W = 1000
H = 700
pygame.init()
sc = pygame.display.set_mode((W, H))

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 15

planet1 = planets.Planet(W//2, H//2, YELLOW, 20000, 20, 0, 0)
planet2 = planets.Planet(300, 100, GREEN, 100, 3, 10, 0)
planet3 = planets.Planet(100, 100, RED, 600, 5, 5, 0)
planet1.draw(sc)
planet2.draw(sc)
planet3.draw(sc)
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #sc.fill(BLACK)
    planet2.move([planet1, planet3])
    planet3.move([planet1, planet2])
    planet1.draw(sc)
    planet2.draw(sc)
    planet3.draw(sc)
    pygame.display.update()
    clock.tick(FPS)
