import pygame


class Button:
    def __init__(self, text, pos, clr):
        self.font = pygame.font.SysFont('arial', 20)
        self.text = text
        self.color = clr
        self.bt_surface = self.font.render(f'{self.text}', True, self.color)
        self.pos = pygame.rect.Rect(pos[0], pos[1], self.font.size(self.text)[0], self.font.size(self.text)[1])

    def blit_bt(self, surface):
        surface.blit(self.bt_surface, self.pos)

    def pressed(self, pos):
        if self.pos.collidepoint(pos):
            return True
        else:
            return False
