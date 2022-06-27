print("Welcome to my Partick Thistle Quiz :)")

playing = input("Are you ready to play? A point for right answers, point off for wrong ones. You ready? ").lower()

if playing != "yes" :
    quit()

print("Okay, let's play :-D ")
print("------------------------")

score = 0

#Q1
answer = input("Where do Thistle play? ").lower()
if answer == "firhill" :
    score += 1
    print("Correct :) Your score is " + str(score))
    print("------------------------")
else :
    if score > 0:
        score -= 1
    print("Oops :( , i have to take a point off. Your score is " + str(score))
    print("------------------------")

#Q2
answer = input("Complete the sentence. Thistle play in red and ... " ).lower()
if answer == "yellow" :
    score += 1
    print("Correct :) Your score is " + str(score))
    print("------------------------")
else :
    if score > 0:
        score -= 1
    print("Oops :( , i have to take a point off. Your score is " + str(score))
    print("------------------------")

#Q3
answer = input("Which league do Thistle play in? " ).lower()
if answer == "championship" :
    score += 1
    print("Correct :) Your score is " + str(score))
    print("------------------------")
else :
    if score > 0:
        score -= 1
    print("Oops :( , i have to take a point off. Your score is " + str(score))
    print("------------------------")

#End of Program
print("GAME OVER !!!!!!!!!!!!!! ")
print("You scored " + str(score) + "/3. That was " + str((score / 3) * 100) + "%")