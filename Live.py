game = ""
def welcome(name):
    print('Hello ' + name + ' and welcome to the World of Games (WoG). \nHere you can find many cool games to play.')
    #return 'Hello ' + name + ' and welcome to the World of Games (WoG). Here you can find many cool games to play.'
def load_game():
    #print ('Please choose a game to play:')
    #print ('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    #print ('2. Guess Game - guess a number and see if you chose like the computer')
    #print ('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
    game = int(input("Please choose a game to play: \n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                 "2. Guess Game - guess a number and see if you chose like the computer\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n\n"
                 ":"))
    difficulty = input("Please choose game difficulty from 1 to 5: ")
    # match case
    match game:
        # pattern 1
        case 1:
            print("You have choose to play: Memory Game\ndifficulty level: " + difficulty)
        # pattern 2
        case 2:
            print("You have choose to play: Guess Game\ndifficulty level: " + difficulty)
        # pattern 3
        case 3:
            print("You have choose to play: Currency Roulette\ndifficulty level: " + difficulty)
        # default pattern
        case _:
            print("Game option should be between 1 and 3")