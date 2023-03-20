import random

options = ("rock", "paper", "scissors")

user_option = input(" Choose: rock, paper, scissors =>")
user_option = user_option.lower()

if not user_option in options:
    print("Error, choose a correct option: rock, paper, scissors ")
    
    user_option = input(" Choose: rock, paper, scissors =>")

computer_option = random.choice(options)

print("User option =>", user_option)
print("Computer option =>", computer_option)

if user_option == computer_option:
    print("Tie!!")

elif user_option == "rock":
    if computer_option == "scissors":
        print("rock beats scissors")
        print("user wins!!!")
    else:
        print("paper beats rock")
        print("computer wins!!!")

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
