from ai import AI
from human import Human

Gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class Game():
    def __init__(self):
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.best_of_rounds = 2
        self.P1 = None
        self.P2 = None
        self.P1_current_score = 0
        self.P2_current_score = 0

      
        


    def run_game(self):
        self.game_start()
        self.game_run()
        self.display_winner()        


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
            self.P2 = AI('AI')
        elif self.start == "2":
            self.P1 = Human('Player1')
            self.P2 = Human('Player2')
        elif self.start == "3":
            self.P1 = AI("Player 1")
            self.P2 = AI("Player 2")
        else:
            print("Please enter a valid key.")
        
       



    def game_run(self):
        while self.P1_current_score == 0 and self.P2_current_score == 0:
            if self.P1.choose_gestures() == self.P2.choose_gestures():
                print("tie")
            elif self.P1.choose_gestures([0]) == "Rock":
                if self.P2.choose_gestures([2]) == "Scissors" or self.P2.choose_gestures([3]) == "Lizard":
                    return self.P1.score_point()
                else:
                    return self.P2.score_point()
            elif self.P1.choose_gestures([1]) == "Paper":
                if self.P2.choose_gestures([0]) == "Rock" or self.P2.choose_gestures([4]) == "Spock":
                    return self.P1.score_point()
                else:
                    return self.P2.score_point()
            elif self.P1.choose_gestures([2]) == "Scissors":
                if self.P2.choose_gestures([1]) == "Paper" or self.P2.choose_gestures([3]) == "Lizard":
                    return self.P1.score_point()
                else:
                    return self.P2.score_point()
            elif self.P1.choose_gestures([3]) == "Lizard":
                if self.P2.choose_gestures([1]) == "Paper" or self.P2.choose_gestures([4]) == "Spock":
                    return self.P1.score_point()
                else:
                    return self.P2.score_point()
            elif self.P1.choose_gestures([4]) == "Spock":
                if self.P2.choose_gestures([2]) == "Scissors" or self.P2.choose_gestures([0]) == "Rock":
                    return self.P1.score_point()
                else:
                    return self.P2.score_point()
            
                

    def display_winner(self):
            if self.P1_current_score > self.P2_current_score:
                print()
                print(f"The winner is {self.P1.name}!")
            elif self.P2_current_score > self.P1_current_score:
                print()
                print(f"The winner is {self.P2.name}! ")
                

