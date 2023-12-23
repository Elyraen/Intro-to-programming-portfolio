from msdie import MSDie

def main():
    die = MSDie(6)
    winning = 0
    continueGame = True

    while continueGame == True:
        die.roll()
        playerAnswer = int(input("Guess the Value of the Die!: "))
        if playerAnswer == die.getValue():
            print ("Correct!")
            winning += 3
            print (f"Your total winnings is ${winning}")
        else:
            print ("WRONG! :(")
            winning -= 1
            print (f"Your total winnings is ${winning}")
    
        playAgain = input("Do you want to continue? (y/n): ").lower()
        if playAgain != "y":
            continueGame = False

main()