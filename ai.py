import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.name = name
              
    def choose_gestures(self):
        self.chosen_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        print(f'{self.name} has picked {gesture_list[int(self.chosen_gesture)]}')
        
        

        