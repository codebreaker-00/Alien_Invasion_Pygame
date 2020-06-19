import sys
import pygame

from time import sleep

from game_stats import Gamestats
from buton import Button
from scoreboard import Scoreboard
from our_ship import ship
from bullet import Bullet
from alien import Alien


background_image = "output-onlinepngtools-min.png"
val = 5

'''def val_upadte():
    val = val + 2'''

class AlienInvasion:
    #It's a master class
    def __init__(self):
        pygame.init() #Initializing the game

        self.screen = pygame.display.set_mode((800,600)) 
        # sets a 1200 pixel wide and 800 pixels high screen called surface
        # Surface returned by pygame.display.set_mode() represents entire game window
        self.bg = pygame.image.load(background_image)
        pygame.display.set_caption("Alien Invasion")

        self.stats = Gamestats(self) # creating instanc to store game-stats
        self.sb =Scoreboard(self)

        self.alien_speed = 1
        self.Ship = ship(self)
        self.our_speed = 1
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.fleet_direction = 1
        self.val = 5
        self._create_fleet()

        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3

        self.play_button = Button(self,"Play")
        #self.win_button = Button(self,"You Won!!")
        #self.Ship_speed = 2

    def _create_fleet(self):
        alien = Alien(self)
        #self.aliens.add(alien)

        #alien_width = 70
        available_space_x = 800 
        number_aliens_x = available_space_x // (140)

        ship_height = self.Ship.rect.height
        alien_width, alien_height = alien.rect.size    

        available_space_y = 600 - (3 * alien_height) - ship_height
        number_rows = available_space_y // (alien_height)

        #print(number_rows)
        #print(number_aliens_x)

        for alien_row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number,alien_row)

    def create_alien(self,alien_number,alien_row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x =  alien_width * alien_number + 50
        alien.rect.x = alien.x
        alien.rect.y =  alien_height * alien_row

        self.aliens.add(alien)

    def _update_aliens(self):

        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.newer_update()
                break

        self.aliens.update(self.fleet_direction)

    def newer_update(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.val#note that you can't increment with value < 1

        self.fleet_direction *= -1
        self.aliens.update(self.fleet_direction)

    def _ship_newwave(self):

        #print(self.stats.ship_left)

        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            self.val *= 1.5
            self.bullet_speed *= 1.5
            self.alien_speed *= 2 
            self.our_speed *= 2
            self.sb.stats.level += 1
            self.sb.prep_level()
            #val_upadte()
        
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.Ship.center_ship()

            sleep(0.5)

        else :
            self.stats.game_active = False
            #self.win_button.draw_button()
            pygame.mouse.set_visible(True)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.game_active = True

            self.stats.reset_stats()
            #print(self.stats.score)
            self.sb.prep_level()
            self.sb.prep_score()
            pygame.mouse.set_visible(False)

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.Ship.center_ship()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self.stats.game_active = False
                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                break


    def run_game(self): # Game is controlled by this function
        self.stats.reset_stats()

        while (True): #Infinte loop until game gives order to quit
            for event in pygame.event.get():
                #pygame.event.get() function returns a list of events occured since the last time it was called 
                if event.type == pygame.QUIT :
                    sys.exit() 
                
                elif event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.Ship.moving_right = True

                    elif event.key == pygame.K_LEFT:
                        self.Ship.moving_left = True

                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullet(self)
                        self.bullets.add(new_bullet)

                    elif event.key == pygame.K_q:
                        sys.exit()
                    
                
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        self.Ship.moving_right = False

                    elif event.key==pygame.K_LEFT:
                        self.Ship.moving_left = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.stats.reset_stats()
                    self._check_play_button(mouse_pos)

            
            if self.stats.game_active:
                self.Ship.update()   
                self.bullets.update()
                self._update_aliens()

          

            self.screen.blit(self.bg,[0,0])
            self.Ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

            for bullet in self.bullets.copy(): #To save memory
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            
            if collisions:
                self.stats.score += 50
                self.sb.prep_score()
                self.sb.check_highscore()
                
            #print(len(self.bullets))
            #print(len(self.bullets))
            self.sb.show_scorecard()

            if not self.aliens:
                # Destroy existing bullets and create new fleet.
                self.bullets.empty()
                #self._create_fleet()
                self._ship_newwave()

            if pygame.sprite.spritecollideany(self.Ship, self.aliens):
                self.stats.game_active = False
                pygame.mouse.set_visible(True)
                


            self._check_aliens_bottom()

            if not self.stats.game_active: #remember to keep it just before flip() func
                self.play_button.draw_button()
                pygame.mouse.set_visible(True)
                #self.stats.reset_stats()
                #self.sb.prep_score()
                #self.sb.prep_level()
                

            pygame.display.flip() # Makes the most recently drawn screen visible
'''
    def _fire_bullet(self):
        if len(self.bullets) < self.bullet_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) '''

            

if __name__ == '__main__' :
    # Make instance and start
    ai = AlienInvasion()
    ai.run_game()

