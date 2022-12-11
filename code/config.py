import pygame
'''
WINDOW_SIZE : 1024 * 576
MAP_SIZE : 1920 * 
'''
#COMMON_CONFIG
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 576
MAP_WIDTH = 1920
MAP_HEIGHT = 1280
FPS = 60
TILE_SIZE = 64
BACKGROUND_COLOR = (0, 255, 127)

#PLAYER_CONFIG
PLAYER_MOVE_SPEED = 2
PLAYER_MOVE_ANIMATION_SPEED = 0.2

#RECT_CONFIG
ENTRY_RECT_X = 1 * TILE_SIZE
ENTRY_RECT_Y = 8 * TILE_SIZE
ENTRY_RECT_W = TILE_SIZE
ENTRY_RECT_H = TILE_SIZE

EXIT_RECT_X = 28 * TILE_SIZE
EXIT_RECT_Y = 15 * TILE_SIZE
EXIT_RECT_W = TILE_SIZE
EXIT_RECT_H = TILE_SIZE

TP_IN_RECT_1_X = 16 * TILE_SIZE
TP_IN_RECT_1_Y = 17 * TILE_SIZE
TP_IN_RECT_1_W = 2 * TILE_SIZE
TP_IN_RECT_1_H = 2 * TILE_SIZE
TP_OUT_RECT_1_X = 15 * TILE_SIZE
TP_OUT_RECT_1_Y = 5 * TILE_SIZE

TP_IN_RECT_2_X = 2 * TILE_SIZE
TP_IN_RECT_2_Y = 1 * TILE_SIZE
TP_IN_RECT_2_W = TILE_SIZE
TP_IN_RECT_2_H = TILE_SIZE
TP_OUT_RECT_2_X = 28 * TILE_SIZE
TP_OUT_RECT_2_Y = 9 * TILE_SIZE

TP_IN_RECT_3_X = 17 * TILE_SIZE
TP_IN_RECT_3_Y = 1 * TILE_SIZE
TP_IN_RECT_3_W = 2 * TILE_SIZE
TP_IN_RECT_3_H = 2 * TILE_SIZE
TP_OUT_RECT_3_X = 19 * TILE_SIZE
TP_OUT_RECT_3_Y = 13 * TILE_SIZE

#EVENT_CONFIG
EVENT_EXIT_GAME = pygame.USEREVENT
EVENT_ENTRY = pygame.USEREVENT + 1
EVENT_TP_1 = pygame.USEREVENT + 2
EVENT_TP_2 = pygame.USEREVENT + 3
EVENT_TP_3 = pygame.USEREVENT + 4
EVENT_TP_AREA = pygame.USEREVENT + 5
EVENT_EXIT = pygame.USEREVENT + 6

#TEXTS_CONFIG
ENTRY_TEXTS = ['You are an explorer named Ezreal',
               'You are exploring a WOODS MAZE!',
               'Try to find the exit of the maze',
               'Press H to get help',
               'Now you\'ve arrived at the first area']
HELP_TEXTS = ['Press the direction keys to move',
              'Press U to increase the volume of bgm',
              'Press D to reduce the volume of bgm',
              'Press ESC to EXIT',
              'There are four areas in the maze',
              'try to get to the next area']
TP_TEXTS = ['Press SPACE to be teleported',
            'to the next AREA']
TP_1_TEXTS = ['Now you\'ve arrived at',
              'the second area']
TP_2_TEXTS = ['Now you\'ve arrived at',
              'the third area']
TP_3_TEXTS = ['Now you\'ve arrived at',
              'the fourth area']
EXIT_TEXTS = ['Congratulations!!!',
              'You\'ve found the exit of the maze!',
              'Press ESC to EXIT']
