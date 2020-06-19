import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    # A class to manage bullets from the space ships

    def __init__(self,ai_game):
        # Create new bullet at the current position of the Ship
        super().__init__()
        self.screen = ai_game.screen
        self.color = ai_game.bullet_color
        self.width = ai_game.bullet_width
        self.height = ai_game.bullet_height
        self.speed = ai_game.bullet_speed

        self.rect = pygame.Rect(ai_game.Ship.rect.x,ai_game.Ship.rect.y,self.width,self.height) 
        self.midtop = ai_game.Ship.rect.midtop


        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)