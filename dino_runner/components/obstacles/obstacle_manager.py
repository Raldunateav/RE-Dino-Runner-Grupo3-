import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.bird_obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                cactus_type = "SMALL"
            else:
                cactus_type = "LARGE"
            self.obstacles.append (Cactus(cactus_type))
            self.bird_obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break
        for obstacle in self.bird_obstacles:
            obstacle.update(game.game_speed, self.bird_obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for obstacle in self.bird_obstacles:
            obstacle.draw(screen)