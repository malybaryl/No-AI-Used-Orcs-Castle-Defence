from src.core.AssetsLoader import AssetsLoader
import pygame

class Background:
    def __init__(self):
        assets_loader = AssetsLoader()
        self.assets = assets_loader.get_image("backgrounds")
        self.image_to_show = self.assets[0]

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image_to_show, (0,0))


