import random
from main import name
def gnu():
    low = 1
    high = int(input(f"hey {name} the range of the number to guess i.e. from 1 to _: ".title()))
    feedback = ""
    turns = 0
    
    while feedback != "c":
        random_no = random.randint(low, high)
        print(f"\nMy Number That I am Guessing Is {random_no}\n")
        feedback = input("enter choice\n(c) if the no is correct\n(h) if the no is too high\n(l) if the number is too low: ")
        if feedback in "hH":
            high = random_no - 1
        elif feedback in "lL":
            low = random_no + 1
        elif feedback in "cC":
            pass
        else:
            print("Not a valid choice")
        
        turns +=1

    print("YAY! i guessed the no correctly in {turns} turns.")


        



def gnc():
    high = int(input("enter the range of the number to guess i.e. from 1 to _: ".title()))
    random_no = random.randint(1, high)

    guess = 0
    turns = 0
    while guess != random_no:
        guess = int(input(f"\nGuess the no between 1 and {high}: "))
        if guess > random_no:
            print("you are too high guess again.".title())
        elif guess < random_no:
            print("you are too low guess again.".title())
        turns += 1
    
    print(f"/nYAY you Win the no was {guess}!\nAnd it took you {turns} turns")




def guess_no():
    print("\nHello welcome to GUESS THE NUMBERR!\nWe Have 2 Modes To Play")
    print("1. Here You Will Think Of A Number And I(The Computer) Will Guess It")
    print("2. Here I Will Think Of A Number And You(The Player) Will Guess It")
    x = input("enter the number of the gamemode you want to play: ".title())
    try:
        x = int(x)
        if x not in [1,2]:
            print("\n\nplease enter a valid game number\n\n".upper())
            guess_no()
    except:
        print("\n\nplease enter a valid game number\n\n".upper()) 
        guess_no()

    if x == 1:
        gnu()
    else:
        gnc()
    


        

if __name__ == "__main__":
    guess_no()