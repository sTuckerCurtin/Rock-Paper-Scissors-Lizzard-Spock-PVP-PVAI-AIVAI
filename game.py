Gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]



class Game():
    def __init__(self):
        self.human = human
        self.player = player 
        self.ai = aiplayer



    def game_start(self):
        print()
        print("Welcome to another game of ROCK, PAPER, SCISSORS, LIZARD, SPOCK")
        print ()
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
            pass
        elif self.start =="2":
            pass
        elif self.start == "3":
            pass
        else:
            "Please enter a different key."
            
        # self.list = print(f" 1.{Gestures[0]}, 2.{Gestures[1]}, 3.{Gestures[2]} 4.{Gestures[3]}, 5.{Gestures[4]}")



    def game_run(self):
        while self.player1_score <2 and self.player2_score <2:
            


        