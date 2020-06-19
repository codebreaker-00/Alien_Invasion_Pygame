import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("Webp.net-resizeimage.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.fleet_direction = 1
        self.speed = ai_game.alien_speed

        #start new alien at top left screen
        self.x=self.rect.x  #self.x
        self.y=self.rect.y  #self.y

        self.x = float(self.rect.x)

        #available_space_x = 800 - (2*alien_width)
        #number_aliens_x = available_space_x // (2*alien_width)


    def check_edge(self):
        # To check if UFO's don't cross the edge of the screen
        screen_rect = self.screen.get_rect()

        #print(screen_rect.right)
        #print (self.rect.right)
        #print (screen)

        #print(self.rect.right)
        #print(self.rect.left)

        if self.rect.right >= screen_rect.right+10 or self.rect.left<=-10 :
            return True

        
    def update(self,fleet_direction):
        self.x += 1*fleet_direction
        self.rect.x =self.x