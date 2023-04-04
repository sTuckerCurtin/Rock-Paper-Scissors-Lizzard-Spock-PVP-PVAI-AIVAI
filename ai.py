
import random
from player import Player

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name
              
    def choose_gesture(self):
        return random.choice(self.gesture_options)
        

        