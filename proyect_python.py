user_option = input("rock, paper, scissors =>")
computer_option = "paper"

if user_option == computer_option:
    print("Tie!!")

elif user_option == "rock":
    if computer_option == "scissors":
        print("rock beats scissors")
        print("user wins!!!")
    else:
        print("paper beats rock")
        print("computer gano!!!")

elif user_option == "paper":
    if computer_option == "rock":
        print("paper beats rock")
        print("user wins!!!!")

    else:
        print("scissors beats paper")
        print("computer wins!!!")

elif user_option == "scissors":
    if computer_option == "paper":
        print("scissors beats paper")
        print("user wins!!!")
    else:
        print("rock beats scissors")
        print("computer wins!!!")
