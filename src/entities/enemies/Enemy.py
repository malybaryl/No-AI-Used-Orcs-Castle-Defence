from src.core.conts import *
from src.entities.LivingEntity import LivingEntity
from src.entities.protectiles.Bullet import Bullet
import pygame
import random

class Enemy(LivingEntity):
    def __init__(self, x = 1, y = 1, max_hit_points = 0, speed = 1, points = []):
        super().__init__(max_hit_points, speed, "enemy", x, y)
        self.cooldown_clock = pygame.time.get_ticks()
        self.cooldown = 1000 / speed
        self.direction = "right"
        self.moving_right = True
        self.points = points
        self.can_move_down = True
        self.cooldown_shoot = random.randint(1000, 10000)
        self.cooldown_shoot_clock = pygame.time.get_ticks()

    def go(self, action):
        if action == "left":
            if self.x//GRID_SIZE > 0:
                self.move(self.x//GRID_SIZE - 1 , self.y//GRID_SIZE)
        if action == "right":
            if self.x//GRID_SIZE < GRID_WIDTH - 1:
                self.move(self.x//GRID_SIZE + 1 , self.y//GRID_SIZE)
        if action == "down":
            if self.y//GRID_SIZE < GRID_HEIGHT:
                self.move(self.x//GRID_SIZE, self.y//GRID_SIZE + 1)
    
    def shoot(self):
        self.attack_animation_state = True
        return Bullet(self.x // GRID_SIZE, self.y // GRID_SIZE, 1,5, True)

    def update(self, endZone = None):
        shoot = None
        end_game = False
        if self.attack_animation_state:
            self.attact_animation(50)

        if endZone:
            if self.rect.colliderect(endZone.rect):
                end_game = True
                return False, shoot, end_game

        if pygame.time.get_ticks() - self.cooldown_shoot_clock > self.cooldown_shoot:
            shoot = self.shoot()
            self.cooldown_shoot_clock = pygame.time.get_ticks()
        
        if not self.points:
            return False, shoot, end_game

        if self.y // GRID_SIZE != self.points[0][1]:
            if self.can_move_down:
                self.direction = "down"
                self.can_move_down = not self.can_move_down
                self.moving_right = not self.moving_right
        elif self.moving_right:
            if self.x // GRID_SIZE < self.points[0][0]:
                self.direction = "right"
        else:
            if self.x // GRID_SIZE > self.points[0][0]:
                self.direction = "left"

        if pygame.time.get_ticks() - self.cooldown_clock > self.cooldown:
            if self.direction == "left":
                self.go(self.direction)
            elif self.direction == "right":
                self.go(self.direction)
            elif self.direction == "down":
                self.go(self.direction)
                self.can_move_down = not self.can_move_down
                if self.moving_right:
                    self.direction = "right"
                else:
                    self.direction = "left"
            self.points.pop(0)
            self.cooldown_clock = pygame.time.get_ticks()

        return False, shoot, end_game    
