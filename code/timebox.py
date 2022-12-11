import pygame.font

from config import *


class TimeBox:
    def __init__(self, start_time):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/joystix.ttf', 25)
        self.start_time = start_time
        self.end_time = pygame.time.get_ticks()

    def display(self, counting):
        surf_1 = self.font.render('TIME:', True, 'White')
        rect_1 = surf_1.get_rect(topleft=(800, 20))
        pygame.draw.rect(self.display_surface, 'Black', rect_1)
        self.display_surface.blit(surf_1, rect_1)

        if counting:
            self.end_time = pygame.time.get_ticks()
        running_time = self.end_time - self.start_time
        minute = str(running_time // 60000)
        second = str(running_time % 60000 // 1000)
        hundredths_of_a_second = str(running_time % 1000 // 10)
        if len(minute) < 2:
            minute = '0' + minute
        if len(second) < 2:
            second = '0' + second
        if len(hundredths_of_a_second) < 2:
            hundredths_of_a_second = '0' + hundredths_of_a_second
        time_str = minute + ':' + second + '.' + hundredths_of_a_second

        surf_2 = self.font.render(time_str, True, 'White')
        rect_2 = surf_2.get_rect(topleft=(800, 60))
        pygame.draw.rect(self.display_surface, 'Black', rect_2)
        self.display_surface.blit(surf_2, rect_2)
