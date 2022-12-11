import pygame.font

from config import *


class PromptBox:
    def __init__(self, texts, pos_x, pos_y):
        self.surfs = []
        self.rects = []
        self.line_num = len(texts)
        self.display_surface = pygame.display.get_surface()
        for i in range(self.line_num):
            self.font = pygame.font.Font('../font/joystix.ttf', 20)
            surf = self.font.render(texts[i], True, 'White')
            self.surfs.append(surf)
            self.rects.append(surf.get_rect(topleft=(pos_x, pos_y + i * 30)))

    def display(self):
        for i in range(self.line_num):
            pygame.draw.rect(self.display_surface, 'Black', self.rects[i])
            self.display_surface.blit(self.surfs[i], self.rects[i])
