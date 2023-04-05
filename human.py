from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        self.name= name 
        
    def score_point(self):
        self.player_one_score = 0
        self.player_two_score = 0
        self.score += 1    
 