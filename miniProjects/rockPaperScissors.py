#Modules
import random

userWins = 0
computerWins = 0

#lists / data structure
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Type Rock/Paper/Scissors or Q to quit ").lower()
    if userInput == "q":
        break

    
    if userInput not in options:
        continue

    randomNumber = random.randint(0,2)
    # 0 - Rock, 1 - Paper, 2 - Scissor
    computerPick = options[randomNumber]
    print("Computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("You won!")
        userWins += 1
    elif userInput == "paper" and computerPick == "rock":
        print("You won!")
        userWins += 1
    elif userInput == "scissors" and computerPick == "paper":
        print("You won!")
        userWins += 1
    else:
        print("You Lost")
        computerWins += 1


print("You won", userWins, "times.")
print("Computer won", computerWins,"times")
print("Goodbyeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee :|")

