class Gamestats:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.game_active = False
        self.level = 1

    def reset_stats(self):
        self.ship_left = 10
        self.score = 0
        self.level = 1