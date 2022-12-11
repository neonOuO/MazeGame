from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, surface=pygame.Surface((TILE_SIZE, TILE_SIZE))):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -30)
