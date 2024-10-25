import random
name = input("Enter Your Name: ")


def rock_paper_scissors():
    print(f"\nHello {name}!!Welcome to Rock Paper And Scissors")
    print("Basic Rules Of Game are:\n1. Rock beats Scissors\n2. Paper beats Rock\n3. Scissors beats Paper\nENJOY!")

    nog = int(input("Enter the no points required to win: "))
    choices = ["r","s","p"]
    points_p = 0
    points_c = 0
    print(f"Player 1 is {name}\nPlayer 2 is computer")
    while True:
        print("\n\n")
        c_choice = random.choice(choices)
        p_choice = input("Enter your choice\n(r) for rock\n(p) for paper\n(s) for scissors\nchoice: ").lower() 
        print(f"\n\n{name}'s choice is {p_choice}")
        print(f"computers's choice is {c_choice}\n\n")
        if c_choice == p_choice:
            points_c += 1
            points_p += 1

            print(f"both chose same so both will get one point\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")      
        elif c_choice == "p" and p_choice == "r":
            points_c += 1
            print(f"Computer Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        elif c_choice == "s" and p_choice == "p":
            points_c += 1
            print(f"Computer Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        elif c_choice == "r" and p_choice == "s":
            points_c += 1
            print(f"Computer Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        elif c_choice == "p" and p_choice == "s":
            points_p += 1
            print(f"{name} Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        elif c_choice == "s" and p_choice == "r":
            points_p += 1
            print(f"{name} Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        elif c_choice == "r" and p_choice == "p":
            points_p += 1
            print(f"{name} Wins!\nupdated points are:\n{name}'s points: {points_p}\nComputer's points: {points_c}")
        else:
            print("not a valic choice.")
        if points_c == points_p == nog:
            print("Tie")
            break
        elif points_c == nog:
            print("Computer Wins!!")
            break
        elif points_p == nog:
            print(f"{name} Wins!!")
            break

        print("\n\n")

    



if __name__ == "__main__":
    rock_paper_scissors()