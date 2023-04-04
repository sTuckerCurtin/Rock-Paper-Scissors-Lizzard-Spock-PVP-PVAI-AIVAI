from player import Player
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
            self.player = Human('Player1')
            self.ai = AI()
        elif self.start == "2":
            self.player = Human('Player1')
            self.player2 = Human('Player2')
        elif self.start == "3":
            self.ai = AI("Player 1")
            self.ai = AI("Player 2")
        else:
            print("Please enter a valid key.")
            
        # self.list = print(f" 1.{Gestures[0]}, 2.{Gestures[1]}, 3.{Gestures[2]} 4.{Gestures[3]}, 5.{Gestures[4]}")



    def game_run(self):
        while self.player_one.points <2 and self.player_two.points <2:
            if self.player.prompt == player_two_gesture:
                return "tie"
            elif player_one_gesture == "Rock":
                if player_two_gesture == "Scissors" or player_two_gesture == "Lizard":
                    return "player one wins"
                else:
                    return "player two wins"
            elif player_one_gesture == "Paper":
                if player_two_gesture == "Rock" or player_two_gesture == "Spock":
                    return "player one wins"
                else:
                    return "player two wins"
            elif player_one_gesture == "Scissors":
                if player_two_gesture == "Paper" or player_two_gesture == "Lizard":
                    return "player one wins"
                else:
                    return "player two wins"
            elif player_one_gesture == "Lizard":
                if player_two_gesture == "Paper" or player_two_gesture == "Spock":
                    return "player one wins"
                else:
                    return "player two wins"
            elif player_one_gesture == "Spock":
                if player_two_gesture == "Scissor" or player_two_gesture == "Rock":
                    return "player one wins"
                else:
                    return "player two wins"
            

