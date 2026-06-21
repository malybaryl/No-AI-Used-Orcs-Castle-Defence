from src.core.AssetsLoader import AssetsLoader
from src.core.conts import *
import pygame

class LivingEntity:
    def __init__(self, max_hit_points, speed, assetName, x, y):
        self.max_hit_points = max_hit_points
        self.hit_points = self.max_hit_points
        self.x = 0
        self.y = 0
        self.speed = speed
        assets_loader = AssetsLoader()
        self.assets = assets_loader.get_image(assetName)
        self.image_to_show = self.assets[0]
        sprite_size = self.assets[0].get_size()
        self.rect = pygame.Rect(0,0,sprite_size[0],sprite_size[1])
        self.rect.center = (self.x, self.y)
        self.move(x,y)
        self.attack_animation_cooldown_timer = pygame.time.get_ticks()
        self.attack_animation_frame = 0
        self.attack_animation_state = False
    
    def attact_animation(self, animation_cooldown = 25):
        animation_size = len(self.assets)
        if animation_size <= 1:
            return

        if pygame.time.get_ticks() - self.attack_animation_cooldown_timer > animation_cooldown:
            self.attack_animation_frame += 1
            if self.attack_animation_frame >= animation_size:
                self.attack_animation_frame = 0
                self.attack_animation_state = False
            self.image_to_show = self.assets[self.attack_animation_frame]
            self.attack_animation_cooldown_timer = pygame.time.get_ticks()


    def move(self, x, y):
        self.x = x * GRID_SIZE 
        self.y = y * GRID_SIZE
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.attack_animation_state:
            self.attact_animation()
        return False

    def draw(self, surface):
        surface.blit(self.image_to_show, (self.rect.center[0],self.rect.center[1]))
