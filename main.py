from src.core.conts import *
from src.core.EnemyManager import EnemyManager
import pygame
import os
import sys
from src.entities.player.Player import Player
from src.entities.enemies.Enemy import Enemy
from src.entities.protectiles.Bullet import Bullet 
from src.entities.Entity import Entity
from src.ui.Background import Background

class App():
    def __init__(self):
        pygame.init()
        self.game_is_on = True
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        game_init = True
        self.clock = pygame.time.Clock() 
        self.key_cooldown_timer = pygame.time.get_ticks()
        self.key_cooldown = 200       
        self.enemy_manager = EnemyManager()

        self.objects = {
                "backgrounds": Background(),
                "protectiles": [],
                "objects": [Entity(x = 3, y = 5, assetName = None, size = (64,32)),
                            Entity(x = 12, y = 5, assetName = None, size = (64,32))],
                "enemies": [],
                "player": Player(5,1,GRID_WIDTH//2,GRID_HEIGHT - 1),
                "end_zone": Entity(x = 14, y = 5, assetName = None, size = (64, 64))
                }

    def run(self):
        while self.game_is_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_on = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if pygame.time.get_ticks() - self.key_cooldown_timer > self.key_cooldown:
                                try:
                                    self.objects["player"].go("left")
                                except:
                                    pass
                                self.key_cooldown_timer = pygame.time.get_ticks()
                        if event.key == pygame.K_RIGHT:
                            if pygame.time.get_ticks() - self.key_cooldown_timer > self.key_cooldown:
                                try:
                                    self.objects["player"].go("right")
                                except:
                                    pass
                                self.key_cooldown_timer = pygame.time.get_ticks()

                        if event.key == pygame.K_SPACE:
                            if pygame.time.get_ticks() - self.key_cooldown_timer > self.key_cooldown:
                                self.objects["protectiles"].append(self.objects["player"].shoot()) 
                                self.key_cooldown_timer = pygame.time.get_ticks()

            self.update()
            self.draw(self.screen)

            scaled_screen = pygame.transform.scale(self.screen, self.window.get_size())
            self.window.blit(scaled_screen, (0, 0))

            pygame.display.update()
            
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()
    
    def update(self):
        for object_class, object in self.objects.items():
            if isinstance(object, list):
                try:
                    for index, object_ in enumerate(object):
                        if not isinstance(object_, Bullet):
                            if not isinstance(object_, Enemy):
                                destroy = object_.update()
                            else:
                                destroy, bullet, end_game = object_.update(self.objects["end_zone"])
                                if bullet:
                                    self.objects["protectiles"].append(bullet)
                                if end_game:
                                    self.game_is_on = False
                        else:
                            destroy, end = object_.update(self.objects)
                            if end:
                                self.game_is_on = False
                        if destroy:
                            object.pop(index)
                except AttributeError:
                    pass
            else:
                try:
                    destroy = object.update()
                    if destroy:
                        pass
                except AttributeError:
                    pass

        enemy = self.enemy_manager.update()
        if enemy:
            self.objects["enemies"].append(enemy)
     
    def draw(self, surface):
        for object_class, object in self.objects.items():
            if isinstance(object, list):
                try:
                    for object_ in object:
                        object_.draw(surface)
                except AttributeError:
                    pass
            else:
                try:
                    object.draw(surface)
                except AttributeError:
                    pass


if __name__ == "__main__":
    app = App()
    app.run()
