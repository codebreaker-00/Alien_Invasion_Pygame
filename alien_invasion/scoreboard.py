import pygame.font

class Scoreboard:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        level_str =str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,(0,0,255))

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str,True,self.text_color,(0,255,0))

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.score_rect.right - 400
        self.high_score_rect.top = self.score_rect.top
        #self.

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,self.text_color, (255,0,0))

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_scorecard(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_highscore(self):

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()