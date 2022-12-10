import pygame

from dino_runner.utils.constants import FONT_STYLE


class Dead:
    def __init__(self):
        self.death_counter = 0

    def update (self):
        self.death_counter += 1 
        

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_component = font.render(f"deaths: {self.death_counter}", True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (1000, 70)
        screen.blit(text_component,text_rect)

    
    