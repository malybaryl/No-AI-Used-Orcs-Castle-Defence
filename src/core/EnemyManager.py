from src.entities.enemies.Enemy import Enemy
from src.core.conts import *
from src.core.singleton import singleton
import pygame

@singleton
class EnemyManager:
    def __init__(self):
        self.points = []
        self.depth = 3
        self.init_path()
        self.cooldown = 2000
        self.cooldown_clock = pygame.time.get_ticks()

    
    def get_points(self):
        return self.points

    def init_path(self):
        y = 0
        x = 0
        for i in range(self.depth):
            for x in range(GRID_WIDTH):
                self.points.append([x, y])
            y += 1
            self.points.append([x,y])
            for x in range(GRID_WIDTH - 1,-1,-1):
                self.points.append([x,y])
            y += 1

    def spawn_enemy(self):
        return Enemy(x = 0, y = 0, max_hit_points = 1, speed = 1, points = self.points.copy())

    def update(self):
        if pygame.time.get_ticks() - self.cooldown_clock > self.cooldown:
            self.cooldown_clock = pygame.time.get_ticks()
            return self.spawn_enemy()
        return None

    def draw(self, surface):
        pass
