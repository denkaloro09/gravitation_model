import pygame
import math

G = 1


class Planet:
    def __init__(self, x, y, clr, m, r, vx, vy):
        self.pos = pygame.Rect(x, y, 2*r, 2*r)
        self.mass = m
        self.vector = Vector(vx, vy)
        self.clr = clr

    def draw(self, surface):
        pygame.draw.circle(surface, self.clr, (self.pos.x, self.pos.y), self.pos.w/2)

    def move(self, list_of_planets):
        for plt in list_of_planets:
            if not(plt is None):
                r = self.find_distance(plt)
                a = G*plt.mass/(r**2)
                d_x = (a / r) * (plt.pos.x - self.pos.x)
                d_y = (a / r) * (plt.pos.y - self.pos.y)
                self.vector.sum_vector(d_x, d_y)
        self.pos.x += self.vector.x
        self.pos.y += self.vector.y

    def find_distance(self, plt):
        return round(math.sqrt((self.pos.x - plt.pos.x)**2 + (self.pos.y - plt.pos.y)**2))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum_vector(self, x, y):
        self.x += x
        self.y += y

    def is_zero_vector(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def cos_between_vectors(self, v):
        ma = math.sqrt(self.x**2 + self.y**2)
        mb = math.sqrt(v.x**2 + v.y**2)
        sc = self.x * v.x + self.y * v.y
        return sc/(ma * mb)

