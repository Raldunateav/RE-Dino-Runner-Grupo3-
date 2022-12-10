import random
from dino_runner.components.obstacles.obstacle_bird import ObstacleBird

class Bird(ObstacleBird):
    def __init__(self, images):
        self.type = random.randint(0,1)
        super().__init__(images, self.type)
        self.rect.y = 270