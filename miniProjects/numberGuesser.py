# Module
import random

# r = random.randint(-5, 11)
# print(r)

## Asking user for a random number
topOfRange = input("Type a number: ")
if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    if topOfRange <= 0:
        print("Please type a number larger than 0.")
        quit()

else:
    print("Please type a number next time")
    quit()


## Using the users number as the max number, create a random number with 0 as the floor and ask the user to guess it.
## I will also track the amount of guesses(line 26), and check to make sure the input is a number(line 28)
randomNumber = random.randint(0, topOfRange)
guesses = 0
while True:
    guesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)

    else:
        print("Please type a number next time")
        continue
        #continue returns to the top of the loop

    if userGuess == randomNumber:
        print("You guessed correctly")
        break
    elif userGuess > randomNumber:
        print("You were above the number!")
    else:
        print("You were below the number")

print("You got it in", guesses,"guesses")