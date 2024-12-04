import random
k="y"
while k=="y" or k== "Y" :
    print("Welcome to Rock, Paper, Scissors Game !")

    choice = int( input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))


    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    lot=[rock,paper,scissors]

    if choice ==0:
        user=rock
        print("You choose")
        print(user)
        print("Computer Choose :")
        computer= random.choice(lot)
        print(computer)

        print("The Result is :")
        if computer==paper:

            print("You lost")
        elif computer==rock:
            print("The game is draw")
        else :
            computer=scissors
            print("You won")
    elif choice ==1:
        user=paper
        print("You choose")
        print(user)
        print("Computer Choose :")
        computer= random.choice(lot)
        print(computer)
        print("The Result is :")
        if computer==paper:
            print("The game is draw")
        elif computer==rock:
            print("You won")


        else :
            computer = scissors
            print("You lost")
    elif choice == 2:
        user = scissors
        print("You choose")
        print(user)
        print("Computer Choose :")
        computer = random.choice(lot)
        print(computer)
        print("The Result is :")
        if computer == paper:
            print("You won")
        elif computer == rock:
            print("You lost")



        else:
            computer = scissors
            print("The game is draw")

    else:
        print("#############################################################################\n")
        print("Out of the range!\nPlease Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
        print("#############################################################################\n")
    k = input("Would you like to restart the game? y / n")
print("Thank you for playing our simple game")



