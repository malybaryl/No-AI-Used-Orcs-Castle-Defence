from src.entities.LivingEntity import LivingEntity
from src.core.conts import *
from src.entities.protectiles.Bullet import Bullet

class Player(LivingEntity): 
    def __init__(self, max_hit_points, speed, x, y):
        super().__init__(max_hit_points, speed, "player", x, y)

    def go(self, action):
        if action == "left":
            if self.x//GRID_SIZE > 0:
                self.move(self.x//GRID_SIZE - self.speed , self.y//GRID_SIZE)
        if action == "right":
            if self.x//GRID_SIZE < GRID_WIDTH - 1:
                self.move(self.x//GRID_SIZE + self.speed , self.y//GRID_SIZE)
        

    def shoot(self):
        self.attack_animation_state = True
        return Bullet(self.x // GRID_SIZE, self.y // GRID_SIZE, 1,5,False)


