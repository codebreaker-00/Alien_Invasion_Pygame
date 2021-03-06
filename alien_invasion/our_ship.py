import pygame

class ship:
    # Here is our player

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #self.settings = ai.settings

        self.image = pygame.image.load('kindpng_460845_1_50x50.png')
        self.rect = self.image.get_rect()

        self.speed = 1

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #Movement Flags
        self.moving_right=False
        self.moving_left= False

    def update(self):
        if (self.moving_right and self.rect.right < self.screen_rect.right):
            self.rect.x += 1

        if (self.moving_left and self.rect.left > 0) :
            self.rect.x -= 1

        #self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
