from src.core.conts import *
from src.core.singleton import singleton
import os
import pygame

@singleton
class AssetsLoader:
    def __init__(self):
        self.images = {}
        self.load_images()
    
    def load_image(self, path):
        return pygame.image.load(BASE_IMG_PATH + path).convert_alpha()

    def load_images(self):
        dir_names = os.listdir("./" + BASE_IMG_PATH)
        for dir in dir_names:
            images_names = os.listdir("./" + BASE_IMG_PATH + dir)
            tmp_images_list = []
            for image in images_names:
                if image.endswith(".png"):
                    tmp_images_list.append(self.load_image(dir + "/" + image))
            self.images.update({dir : tmp_images_list})

    def get_images(self):
        return self.images

    def get_image(self, name):
        return self.images.get(name)


