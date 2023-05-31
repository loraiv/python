from typing import Any
import pygame
from settings import *


class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load('sky.png').convert()

        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image,(full_width, full_height))

        self.image = pygame.Surface((full_width * 2, full_height))
        self.image.blit(full_sized_image, (0, 0))
        self.image.blit(full_sized_image, (full_width, 0))

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, delta_time):
        self.position.x -= 300 * delta_time
        self.rect.centerx = round(self.position.x)
        if self.rect.right <= 0:
            self.position.x = 0
        self.rect.x = round(self.position.x)

class Ground(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)\
        
        # imade
        ground_surface = pygame.image.load('grass.png').convert()
        self.image = pygame.transform.scale(ground_surface, pygame.math.Vector2(ground_surface.get_size()) * scale_factor)
        
        # positiom
        self.rect = self.image.get_rect(bottomleft = (0,WINDOW_HEIGHT))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def update(self, delta_time):
        self.position.x -= 370 * delta_time
        if self.rect.centerx <= 0:
            self.position.x = 0

        self.rect.x = round(self.position.x)

class Plane(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)

        # image
        self.import_frames(scale_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]


        #rect
        self.rect = self.image.get_rect(midleft = (WINDOW_WIDTH / 20, WINDOW_HEIGHT / 2))
        self.position = pygame.math.Vector2(self.rect.topleft)

        # movement
        self.gravity = 250
        self.direction = 0

    def import_frames(self, scale_factor):

        self.frames = []
        for i in range(3):
            surf = pygame.image.load('plane1.png').convert_alpha()
            scaled_surface = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scale_factor)
            self.frames.append(scaled_surface)

    def apply_gravity(self, delta_time):
        self.direction += self.gravity * delta_time
        self.position.y += self.direction * delta_time
        self.rect.y = round(self.position.y)

    def jump(self):
        self.direction = -400

    def update(self, delta_time):
        self.apply_gravity(delta_time)
        # self.animate(delta_time)
        # self.rotate(delta_time)