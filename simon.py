# This is a sample Python script.
import random

class Simon:
    single_vals = list()
    double_vals = list()
    triple_vals = list()
    game_length = 8 #TODO config file

    def menu(self):
        # Simon Says:
        # 1 Singles
        # 2 Doubles
        # 3 Triples
        # 4 All
        # 9 Preferences
        # 0 Exit
        print("Simon Says: Choose mode.")
        print("1 Singles")
        print("2 Doubles")
        print("3 Triples")
        print("4 Mix All")
        print("5 Preferences")
        print("6 Exit")
        try:
            sel = input("Enter option #: ")
        except:
            pass

    def single(self, game_length:int =8, *bank):
        key = [] # answer key
        print(f'Simon Says, {game_length} Rounds')
        for round in range(game_length):
            key.append( random.choice(bank) )
            print(list(key))
            ## clear screen *
            guess_str = input() ##TODO replace with button press
            guess = list(guess_str)
            if guess != key:
                #Buzzer
                print("Game Over.")
                exit(0)
            #Ding!
        print("You Win!")
        exit(0)
    def double(self):
        pass
    def triple(self):
        pass
    def all(self):
        pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Simon()
    a.single(4, 'a','s','d','f')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
