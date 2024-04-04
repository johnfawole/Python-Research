import sys
import random

print("")

gamerpreference = input("Enter... \n1 for John, \n2 for Grace, or \n3 for Junior:\n\n" )
gamer = int(gamerpreference)

if gamer < 1 or gamer > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)

print ("")
print ("You chose " + gamerpreference + ".")
print ("John chose " + computerchoice + ".")
print("")

if gamer == 1 and computer == 3:
    print("you are the boss!")
elif gamer == 2 and computer == 1:
    print("you are the boss!")
elif gamer == 3 and computer == 2:
    print("you are the boss!")
elif gamer == computer:
    print("hmmmm, there is a tie~")