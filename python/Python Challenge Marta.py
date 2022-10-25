import random


computerScore = 0   #those are the score tracking variables
playerScore = 0

while True:    #game cycle
    print("""The winning Rules are as follows:
    Rock smashes Scissors.
    Paper covers Rock.
    Scissors cut Paper.""")

    rpsList = ["r", "p", "s"]                 #the list of options the computer can randomly pick from
    computerchoice = random.choice(rpsList)
    choice=input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ")
    if choice != "r" and choice != "p" and choice != "s":   #this is a control check in case something different from r, s, p is typed
        print("You can only choose between r, p and s")
        continue
    elif computerchoice == choice:     #this is the condition of a tie
        print("the computer chose: %s you chose: %s. That's a tie" % (computerchoice, choice))


    else:                  #I only listed the player's winning conditions in this, they all update the player's score
        if computerchoice == "r" and choice == "p":
            print("the computer chose: %s you chose: %s. You won!" % (computerchoice, choice))
            playerScore+=1


        elif computerchoice == "p" and choice == "s":
            print("the computer chose: %s you chose: %s. You won!" % (computerchoice, choice))
            playerScore += 1


        elif computerchoice == "s" and choice == "r":
            print("the computer chose: %s you chose: %s. You won!" % (computerchoice, choice))
            playerScore += 1


        else:    #so that every other condition means the player has lost and the computer's score gets updated
            print("the computer chose: %s you chose: %s. You lose" % (computerchoice, choice))
            computerScore += 1
    print("""Computer Score: %d
    Player score: %d""" % (computerScore, playerScore))
    play = input("Play again? (y/n)")
    if play == "y":   #if yes is selected the while loop starts again
        continue
    elif play == "n": #when no is selected the break will exit the while loop and terminate the progam
       print("Thanks for playing!")
       break
