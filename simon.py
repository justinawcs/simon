# This is a sample Python script.
import random
import sys
import logging
logging.basicConfig(level=logging.INFO)

class Simon:
    single_vals = list()
    double_vals = list()
    triple_vals = list()
    game_length:int = 8 #TODO config file

    def menu(self):
        working = True
        while working:
            # Simon Says:
            # 1 Singles
            # 2 Doubles
            # 3 Triples
            # 4 All
            # 9 Preferences
            # 0 Exit
            print("\nSimon Says: Choose mode.")
            print("1 Singles")
            print("2 Doubles")
            print("3 Triples")
            print("4 Mix All")
            print("5 Preferences")
            print("6 Exit")
            sel = input("Enter an option> ")
            try:
                sel = int(sel)
                logging.debug("{} {}".format(sel, type(sel) ))
                if sel == 1:
                    print("One")
                elif sel == 2:
                    print("Two")
                elif sel == 3:
                    print("Three")
                elif sel == 4:
                    print("Four")
                elif sel == 5:
                    print("Current Game Length: " + str(self.game_length) )
                    sel2:str = input("Set new game length, or leave blank to Go Back> ")
                    if str(sel2).strip() != "" and int(sel2).is_integer():
                        self.game_length = int(sel2)
                        print("Game length set: " + str(self.game_length))
                    else:
                        pass #break
                elif sel == 6:
                    working = False
                    #sys.exit(0)
                else:
                    print("Bad input. Try again")
            except KeyboardInterrupt:
                sys.exit(0)
            finally:
                pass
        sys.exit(0)

    def engine(self, game_length:int =8, *bank):
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
    def single(self):
        self.engine(game_length=5, )
    def double(self):
        pass
    def triple(self):
        pass
    def all(self):
        pass

    # def takeInput(prompt, expectedType):
    #     if expectedType == int or expectedType == float:
    #         try:
    #             sel = input(prompt + "> ")  # use input to pre-check types
    #         except NameError:
    #             print(expectedType, "was expected, not string" )
    #             return None
    #     else:  # expectedType == string-type
    #         sel = str(prompt + "> ")
    #     if isinstance(sel, expectedType):
    #         # just return it
    #         return sel
    #     elif isinstance(sel, int):  # force float
    #         print(expectedType, "was expected, forced: float")
    #         return float(sel)
    #     elif isinstance(sel, float):  # force int
    #         print(expectedType, "was expected, forced: int")
    #         return int(sel)
    #     else:
    #         print(expectedType, "was expected, not: ", type(sel))
    #         return None

if __name__ == '__main__':
    a = Simon()
    #a.engine(4, 'a','s','d','f')
    a.menu()
