from ai import AI
from human import Human

Gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]



class Game():
    def __init__(self):
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        # self.best_of_rounds = best_of_rounds
        # self.is_multiplayer = is_multiplayer
        self.player_one_score = 0
        self.player_two_score = 0
        self.round_number = 0
        self.player = Human('Player1', 'Player2')
        self.ai = AI('AI')


    def game_start(self):
        print()
        print("Welcome to another game of ROCK, PAPER, SCISSORS, LIZARD, SPOCK")
        print()
        print("Each match will be best of three games. Use the numerator keys to enter your selection.")
        print()     
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard Poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("paper disproves Spock")
        print("Spock vaporizes Rock")
        print()
        
        self.start = input("How many players? 1, 2, or 3 for a surprise. ")
        if self.start == "1":
            self.P1 = Human('Player1')
            self.P2 = AI()
        elif self.start == "2":
            self.P1 = Human('Player1')
            self.P2 = Human('Player2')
        elif self.start == "3":
            self.P1 = AI("Player 1")
            self.P2 = AI("Player 2")
        else:
            print("Please enter a valid key.")
            
        # self.list = print(f" 1.{Gestures[0]}, 2.{Gestures[1]}, 3.{Gestures[2]} 4.{Gestures[3]}, 5.{Gestures[4]}")



    def game_run(self):
        while self.P1.player_one_score <2 and self.P2.player_two_score <2:
            if self.P1.gesture_options == self.P2.gesture_options:
                return "tie"
            elif self.P1.gesture_options == "Rock":
                if self.P2.gesture_options == "Scissors" or self.P2.gesture_options == "Lizard":
                    return "player one wins"
                else:
                    return "player two wins"
            elif self.P1.gesture_options == "Paper":
                if self.P2.gesture_options == "Rock" or self.P2.gesture_options == "Spock":
                    return "player one wins"
                else:
                    return "player two wins"
            elif self.P1.gesture_options == "Scissors":
                if self.P2.gesture_options == "Paper" or self.P2.gesture_options == "Lizard":
                    return "player one wins"
                else:
                    return "player two wins"
            elif self.P1.gesture_options == "Lizard":
                if self.P2.gesture_options == "Paper" or self.P2.gesture_options == "Spock":
                    return "player one wins"
                else:
                    return "player two wins"
            elif self.P1.gesture_options == "Spock":
                if self.P2.gesture_options == "Scissor" or self.P2.gesture_options == "Rock":
                    return "player one wins"
                else:
                    return "player two wins"
            

