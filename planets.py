import pygame
import math

G = 1


class Planet:
    def __init__(self, x, y, clr, m, r, start_vec, state):
        self.pos = pygame.Rect(x, y, 2 * r, 2 * r)
        self.mass = m
        self.vector = Vector(start_vec[0], start_vec[1])
        self.main_clr = clr
        self.track_clr = (clr[0] // 2, clr[1] // 2, clr[2] // 2)
        self.stay = state  # флаг на влияние на планету гравитации от других объектов
        self.clicked = False  # флаг на нажатие мышкой для перемещения
        self.track = True  # флаг для рисования траектории планеты
        self.selected = False  # флаг для выбора планеты
        self.processed = False

    def draw(self, main_surface, track_surface):
        if self.track:
            pygame.draw.circle(track_surface, self.track_clr, (self.pos.x, self.pos.y), self.pos.w / 5)
        pygame.draw.circle(main_surface, self.main_clr, (self.pos.x, self.pos.y), self.pos.w / 2)

    def move(self, list_of_planets):
        if not self.stay:  # если планета не закреплена
            for plt in list_of_planets:
                if not (plt is None) and not plt.processed and id(plt) != id(self):
                    r = self.find_distance(plt)
                    if r != 0:
                        # изменение положения искомой планеты
                        a = G * plt.mass / (r ** 2)
                        d_x = (a / r) * (plt.pos.x - self.pos.x)
                        d_y = (a / r) * (plt.pos.y - self.pos.y)
                        self.vector.sum_vector(d_x, d_y)
                        # изменение положения итерируемой планеты
                        if not plt.stay:
                            plt_a = G * self.mass / (r ** 2)
                            plt_d_x = (plt_a / r) * (self.pos.x - plt.pos.x)
                            plt_d_y = (plt_a / r) * (self.pos.y - plt.pos.y)
                            plt.vector.sum_vector(plt_d_x, plt_d_y)
                        self.processed = True
        self.pos.x += self.vector.x
        self.pos.y += self.vector.y

    def move_by_mouse(self, rel):
        self.pos.move_ip(rel)

    def find_distance(self, plt):
        return round(math.sqrt((self.pos.x - plt.pos.x) ** 2 + (self.pos.y - plt.pos.y) ** 2))

    def is_clicked_by_mouse(self, pos):
        if (pos[0] - self.pos.x) ** 2 + (pos[1] - self.pos.y) ** 2 <= (self.pos.w / 2) ** 2:
            self.clicked = True
        else:
            self.clicked = False
        return self.clicked

    def is_clicked(self):
        return self.clicked

    def not_clicked(self):
        self.clicked = False

    def reset_speed(self):
        self.vector.reset_vector()

    def flip_track(self):
        if self.track:
            self.track = False
        else:
            self.track = True


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

    def reset_vector(self):
        self.x = 0
        self.y = 0

    def cos_between_vectors(self, v):
        ma = math.sqrt(self.x ** 2 + self.y ** 2)
        mb = math.sqrt(v.x ** 2 + v.y ** 2)
        sc = self.x * v.x + self.y * v.y
        return sc / (ma * mb)
