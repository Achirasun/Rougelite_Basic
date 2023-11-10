import pygame
from setting import *
from entity import Entity
from support import import_folder

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./Asset/dungeon/heroes/knight/knight_idle_anim_f0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #movement
        self.speed = 2
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

        # stats (UI)
        self.stats = {'health': 100, 'energy': 60, 'speed': 2}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']

    def import_player_assets(self):
        character_path = f'../Asset/dungeon/heroes/'
        self.animations = {'idle_up':[],'idle_down':[],'idle_left':[],'idle_right':[],
                           'move_up':[],'move_down':[],'move_left':[],'move_right':[],
                           'attack_up':[],'attack_down':[],'attack_left':[],'attack_right':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        """Player Movement input"""
        #Create Key input
        key = pygame.key.get_pressed()

        #get player movement
        if key[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        
        #get player attack
        if key[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
        
        if key[pygame.K_LCTRL] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()

    def get_status(self):
        
        # idel status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = 'idle_' + self.status
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle_', 'attack_')
                else:
                    self.status = 'attack_' + self.status
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('attack', '')

    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        if animation:    
            self.image = animation[int(self.frame_index)]
        else:
            print(f"Empty animation list for status: {self.status}")
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
        
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)