from config import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.animations = {}
        self.import_access()
        self.status = 'down_idle'
        self.frame_index = 0
        self.animation_speed = PLAYER_MOVE_ANIMATION_SPEED
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = PLAYER_MOVE_SPEED
        self.obstacle_sprites = obstacle_sprites
        self.hitbox = self.rect.inflate(0, -25)

    def import_access(self):
        self.animations = {'up_walk': [], 'down_walk': [], 'left_walk': [], 'right_walk': [],
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': []}
        for animation in self.animations.keys():
            full_path = '../graphics/player/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        self.frame_index += self.animation_speed
        animation = self.animations[self.status]
        if int(self.frame_index) >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def if_in_rect(self, rect_left_top_x, rect_left_top_y, rect_w, rect_h):
        rect_right_bottom_x = rect_left_top_x + rect_w
        rect_right_bottom_y = rect_left_top_y + rect_h
        if rect_left_top_x <= self.rect.centerx <= rect_right_bottom_x and rect_left_top_y <= self.rect.centery <= rect_right_bottom_y:
            return True
        return False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if self.if_in_rect(TP_IN_RECT_1_X, TP_IN_RECT_1_Y, TP_IN_RECT_1_W, TP_IN_RECT_1_H):
                self.tp(TP_OUT_RECT_1_X, TP_OUT_RECT_1_Y)
                event = pygame.event.Event(EVENT_TP_1)
                pygame.event.post(event)
            if self.if_in_rect(TP_IN_RECT_2_X, TP_IN_RECT_2_Y, TP_IN_RECT_2_W, TP_IN_RECT_2_H):
                self.tp(TP_OUT_RECT_2_X, TP_OUT_RECT_2_Y)
                event = pygame.event.Event(EVENT_TP_2)
                pygame.event.post(event)
            if self.if_in_rect(TP_IN_RECT_3_X, TP_IN_RECT_3_Y, TP_IN_RECT_3_W, TP_IN_RECT_3_H):
                self.tp(TP_OUT_RECT_3_X, TP_OUT_RECT_3_Y)
                event = pygame.event.Event(EVENT_TP_3)
                pygame.event.post(event)

        if keys[pygame.K_DOWN]:
            self.direction.x = 0
            self.direction.y = 1
            self.status = 'down_walk'
        elif keys[pygame.K_UP]:
            self.direction.x = 0
            self.direction.y = -1
            self.status = 'up_walk'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction.y = 0
            self.status = 'right_walk'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.direction.y = 0
            self.status = 'left_walk'
        else:
            self.direction.x = 0
            self.direction.y = 0

    def move(self):
        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        self.if_in_tp_area()
        self.if_in_exit_area()

    def if_in_tp_area(self):
        if (self.if_in_rect(TP_IN_RECT_1_X, TP_IN_RECT_1_Y, TP_IN_RECT_1_W, TP_IN_RECT_1_H) or
                self.if_in_rect(TP_IN_RECT_2_X, TP_IN_RECT_2_Y, TP_IN_RECT_2_W, TP_IN_RECT_2_H) or
                self.if_in_rect(TP_IN_RECT_3_X, TP_IN_RECT_3_Y, TP_IN_RECT_3_W, TP_IN_RECT_3_H)):
            event = pygame.event.Event(EVENT_TP_AREA)
            pygame.event.post(event)
            return True
        return False

    def if_in_exit_area(self):
        if self.if_in_rect(EXIT_RECT_X, EXIT_RECT_Y, EXIT_RECT_W, EXIT_RECT_H):
            event = pygame.event.Event(EVENT_EXIT)
            pygame.event.post(event)
            return True
        return False

    def tp(self, dst_x, dst_y):
        self.hitbox.x = dst_x
        self.hitbox.y = dst_y
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if 'walk' in self.status:
                self.status = self.status.replace('walk', 'idle')

    def update(self):
        self.input()
        self.move()
        self.get_status()
        self.animate()
