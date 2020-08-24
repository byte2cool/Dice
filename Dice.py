import random

def main():
    print("Welcome to the random number guesser game, dice")
    dice = input("Do you want roll the dice and pick a random number for you? ")
    if dice.lower() == "yes" or dice.lower() == "y":
        print("Rolling the dices....")
        round = 1
        while round != 4:
            print("Rounds " + str(round))
            print("The number is " + roll_dice())
            round = round + 1
            
    elif dice.lower() == "no" or dice.lower() == "n":
        print("Hope you try running me again....bye")
    else:
        print("Give a real answer")
        
        

def roll_dice():
    rolldice = random.randint(1,6)
    return str(rolldice)