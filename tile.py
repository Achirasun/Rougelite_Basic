import pygame
from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups,sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

        # # recommend hitbox by ผม => self.hitbox = self.rect.inflate(0, -10) and (in this line below)
        self.hitbox = self.rect.inflate(0, -5)
