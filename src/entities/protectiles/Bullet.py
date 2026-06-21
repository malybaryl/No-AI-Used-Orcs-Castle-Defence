from src.core.conts import *
import pygame
from src.entities.LivingEntity import LivingEntity

class Bullet(LivingEntity):
    def __init__(self, x = 0, y = 1, damage = 1, speed = 1,enemyBullet = True):
        self.enemyBullet = enemyBullet
        if self.enemyBullet:
            super().__init__(0, speed, "enemyProtectile", x, y)
        else:
            super().__init__(0, speed, "protectile", x, y)
        self.move(x,y)
        self.direction = "down"
        self.cooldown = 1000 / speed
        self.cooldown_clock = pygame.time.get_ticks()
        if enemyBullet == False:
            self.direction = "up"
                
    def move(self, x, y):
        self.x = x * GRID_SIZE + self.rect.width // 2
        self.y = y * GRID_SIZE + self.rect.height // 2
        self.rect.center = (self.x, self.y)


    def update(self, objects = {}):
        player_hit = False
        for object_class, object in objects.items():
            if self.enemyBullet:
                if object_class == "player":
                    if self.rect.colliderect(object.rect):
                        player_hit = True
            else:
                if object_class == "enemies":
                    for index, object_ in enumerate(object):
                        if self.rect.colliderect(object_.rect):
                            object.pop(index)
                            return True, player_hit
            if object_class == "objects":
                for index, object_ in enumerate(object):
                    if self.rect.colliderect(object_.rect):
                        return True, player_hit

        if pygame.time.get_ticks() - self.cooldown_clock > self.cooldown:
            if self.direction == "up":
                self.move(self.x // GRID_SIZE , self.y//GRID_SIZE - 1)
            elif self.direction == "down":
                self.move(self.x // GRID_SIZE, self.y // GRID_SIZE + 1)
            self.cooldown_clock = pygame.time.get_ticks()

        if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
            return True, player_hit
        return False, player_hit

