print("Welcome to my Partick Thistle Quiz :)")

playing = input("Are you ready to play? ").lower()

if playing != "yes" :
    quit()

print("Okay, let's play :-D ")


score = 0

#Q1
answer = input("Where do Thistle play? ").lower()

if answer == "firhill" :
    print("Correct :)")
    score += 1
else :
    print("Incorrect :(")

#Q2
answer = input("Complete the sentence. Thistle play in red and ... " ).lower()
if answer == "yellow" :
    print("Correct Again :)")
    score += 1
else :
    print("Incorrect :(")

#Q3
answer = input("Which league do Thistle play in? " ).lower()
if answer == "championship" :
    print("Correct Again Again :)")
    score += 1
else :
    print("Incorrect :(")

#End of Program
print("Woohoo, You scored " + str(score) + "/3")
print("That was " + str((score / 4) * 100) + "%")