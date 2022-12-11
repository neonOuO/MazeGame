import pygame.time
from tile import Tile
from player import Player
from debug import debug
from support import *
from prompt_box import *
from timebox import *


class Level:
    def __init__(self):
        self.player = None
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()
        self.show_prompt_box = False
        self.show_prompt_box_time = 0
        self.prompt_box = PromptBox('', 10, 10)
        self.box_start_time = None
        self.start_time = pygame.time.get_ticks()
        self.timebox = TimeBox(self.start_time)
        self.counting = True

    def set_prompt_box_box(self, text, pos_x, pox_y, time):
        self.box_start_time = pygame.time.get_ticks()
        self.show_prompt_box = True
        self.show_prompt_box_time = time
        self.prompt_box = PromptBox(text, pos_x, pox_y)

    def set_box_status(self):
        if self.show_prompt_box:
            if pygame.time.get_ticks() - self.box_start_time >= self.show_prompt_box_time:
                self.show_prompt_box = False

    def create_map(self):
        layouts = {
            'trees': import_csv_layout('../map_csv/TiledMap_tree.csv'),
            'objects': import_csv_layout('../map_csv/TiledMap_object.csv')
        }
        graphics = {
            'trees': import_folder('../graphics/trees'),
            'objects': import_folder('../graphics/objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col == '-1':
                        continue
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    if style == 'trees':
                        Tile((x, y), [self.visible_sprites, self.obstacles_sprites], graphics['trees'][int(col)])
                    if style == 'objects':
                        Tile((x, y), [self.visible_sprites, self.obstacles_sprites], graphics['objects'][int(col)])

        self.player = Player((ENTRY_RECT_X, ENTRY_RECT_Y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.set_box_status()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.timebox.display(self.counting)
        if self.show_prompt_box:
            self.prompt_box.display()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.ground_surf = pygame.image.load('../graphics/tiledMap/TiledMap.png').convert()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        ground_offset_pos = self.ground_rect.topleft - self.offset
        if ground_offset_pos.x > 0:
            self.offset.x += ground_offset_pos.x
            ground_offset_pos.x = 0
        if ground_offset_pos.y > 0:
            self.offset.y += ground_offset_pos.y
            ground_offset_pos.y = 0
        if ground_offset_pos.x < WINDOW_WIDTH - MAP_WIDTH:
            self.offset.x += ground_offset_pos.x - (WINDOW_WIDTH - MAP_WIDTH)
            ground_offset_pos.x = WINDOW_WIDTH - MAP_WIDTH
        if ground_offset_pos.y < WINDOW_HEIGHT - MAP_HEIGHT:
            self.offset.y += ground_offset_pos.y - (WINDOW_HEIGHT - MAP_HEIGHT)
            ground_offset_pos.y = WINDOW_HEIGHT - MAP_HEIGHT
        self.display_surface.blit(self.ground_surf, ground_offset_pos)
        for sprite in sorted(self.sprites(), key=lambda x: x.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
