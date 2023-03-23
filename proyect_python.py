import random

options = ("rock", "paper", "scissors")
computer_wins = 0
user_wins =0 

rounds = 1

while True: 

    print("*" * 20)
    print("ROUND", rounds)
    print("*" * 20)

    print("COMPUTER_WINS", computer_wins)
    print("USER_WINS", user_wins)


    user_option = input(" CHOOSE: rock, paper, scissors =>")
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
        print("Error, choose a correct option: rock, paper, scissors ")
        continue
        

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)

    if user_option == computer_option:
        print("Tie!!")

    elif user_option == "rock":
        if computer_option == "scissors":
            print("rock beats scissors")
            print("user wins!!!")
            user_wins += 1
        else:
            print("paper beats rock")
            print("computer wins!!!")
            computer_wins += 1

    elif user_option == "paper":
        if computer_option == "rock":
            print("paper beats rock")
            print("user wins!!!!")
            user_wins += 1

        else:
            print("scissors beats paper")
            print("computer wins!!!")
            computer_wins += 1

    elif user_option == "scissors":
        if computer_option == "paper":
            print("scissors beats paper")
            print("user wins!!!")
            user_wins += 1
        else:
            print("rock beats scissors")
            print("computer wins!!!")
            computer_wins += 1

    if computer_wins == 2:
        print("The winner is the computer")
        break

    if user_wins == 2:
        print("the winner is the user")
        break

    
