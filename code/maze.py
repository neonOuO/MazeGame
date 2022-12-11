import sys
from level import Level
from config import *
from debug import debug


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Woods Maze')
        self.clock = pygame.time.Clock()
        self.level = Level()
        event = pygame.event.Event(EVENT_ENTRY)
        pygame.event.post(event)
        pygame.mixer.music.load('../bgm/bgm.ogg')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        icon = pygame.image.load("../icon/icon.ico")
        pygame.display.set_icon(icon)

    def keys_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            event = pygame.event.Event(EVENT_EXIT_GAME)
            pygame.event.post(event)
        if keys[pygame.K_h]:
            self.level.set_prompt_box_box(HELP_TEXTS, 20, 20, 5000)
        volume = pygame.mixer.music.get_volume()
        delta_volume = 0.02
        if keys[pygame.K_u] and volume + delta_volume <= 1:
            pygame.mixer.music.set_volume(volume + delta_volume)
        if keys[pygame.K_d] and volume - delta_volume >= 0:
            pygame.mixer.music.set_volume(volume - delta_volume)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == EVENT_EXIT_GAME:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENTRY:
                    self.level.set_prompt_box_box(ENTRY_TEXTS, 20, 20, 10000)
                if event.type == EVENT_TP_1:
                    self.level.set_prompt_box_box(TP_1_TEXTS, 20, 20, 5000)
                if event.type == EVENT_TP_2:
                    self.level.set_prompt_box_box(TP_2_TEXTS, 20, 20, 5000)
                if event.type == EVENT_TP_3:
                    self.level.set_prompt_box_box(TP_3_TEXTS, 20, 20, 5000)
                    self.level.player.animation_speed = 0.1
                    self.level.player.speed = 1
                if event.type == EVENT_TP_AREA:
                    self.level.set_prompt_box_box(TP_TEXTS, 20, 20, 100)
                if event.type == EVENT_EXIT:
                    self.level.set_prompt_box_box(EXIT_TEXTS, 20, 20, 1000000)
                    self.level.counting = False

            self.keys_input()
            self.screen.fill(BACKGROUND_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
