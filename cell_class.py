import pygame
from math import sin

class Cell():
    def __init__(self, x, y, w, h, r, g, b, offset):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.offset = offset
        self.rate_of_change = 0.1

        self.r_offset = r
        self.g_offset = g
        self.b_offset = b

        self.color = self.get_colour()

    def get_colour(self):
        r = abs(sin(self.offset + self.r_offset)) * 255
        g = abs(sin(self.offset + self.g_offset)) * 255
        b = abs(sin(self.offset + self.b_offset)) * 255

        return [r, g, b]

    def update(self):
        self.color = self.get_colour()
        self.offset += self.rate_of_change

    def draw(self, screen):
        self.update()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))




