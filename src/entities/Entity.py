from src.core.AssetsLoader import AssetsLoader
from src.core.conts import *
import pygame

class Entity:
    def __init__(self, x, y, assetName = None, size = (0,0)):
        self.x = 0
        self.y = 0
        self.assetName = assetName
        if self.assetName:
            assets_loader = AssetsLoader()
            self.assets = assets_loader.get_image(assetName)
            self.image_to_show = self.assets[0]
            sprite_size = self.assets[0].get_size()
        else:
            sprite_size = size
        self.rect = pygame.Rect(0,0,sprite_size[0],sprite_size[1])
        self.rect.center = (self.x, self.y)
        self.move(x,y)
    
    def move(self, x, y):
        self.x = x * GRID_SIZE 
        self.y = y * GRID_SIZE
        self.rect.center = (self.x, self.y)

    def update(self):
        return False

    def draw(self, surface):
        if self.assetName:
            surface.blit(self.image_to_show, (self.rect.center[0],self.rect.center[1]))
