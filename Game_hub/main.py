from hangman import hangman as hg
from rock_paper_scissor import rock_paper_scissors as rps
from tic_tac_toe import tic_tac_toe as ttt
from guess_no import guess_no as gnu
from menu import menu, logo , loadscr

name = input("Enter your name: ")
loadscr()

play = True

game = menu()

while play:#Main Gamelop
    match game:
        case 1:
            gnu()

        case 2:
            hg()
        case 3:
            rps()
        case 4:
            ttt()
    play = input("\n\ndo you want to continue\ntype 1 to continue and anything else to quit\nenter your choice:  ".title())
    if play == "1":
        game = menu()
    else:
        print("\nthanks for playing\n".upper())
        logo()
        quit()



