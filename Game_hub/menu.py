game_list = [1,2,3,4]

def logo():
    print(" -------------------- ")
    print("|      GAME HUB      |")
    print(" -------------------- ")

def loadscr():
    logo()
    print("\nHELLO WELCOME TO GAME HUB!")
    print("Here you will have multiple games to play. Follow the rules and enjoy!!\n")
    
def menu():
    game=""
    print("We Have The Following Games.")
    print("1. Guess The Number")
    print("2. Hangman")
    print("3. Rock Paper Scissors")
    print("4. Tic Tac Toe")
    game = input("enter the games number which you want to play: ".title())

    
    try:
        game = int(game)
        if game not in game_list:
            print("\n\nplease enter a valid game number\n\n".upper())
            game = menu()
    except:
        print("\n\nplease enter a valid game number\n\n".upper()) 
        game = menu() 
    finally:
        return game




if __name__ == "__main__":
    menu()
