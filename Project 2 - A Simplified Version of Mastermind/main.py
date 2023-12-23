import random

def createCode():
    preString = 'GBRYPO'
    codeLength = 0
    code = ''
    while codeLength < 4:
        code += random.choice(preString)
        codeLength += 1
    return code

def compareStrings(String1, string2):
    counter = 0
    if len(String1) == len(string2):
        print("The strings have the same length!")
        for i in range(len(String1)):
            if String1[i] == string2[i]:
                counter += 1
    else:
        print("The strings can't be compared.")
        counter = -1
    return counter


def main():
    code = createCode()
    gameContinue = True
    incorrectGuesses = 0

    while gameContinue and incorrectGuesses < 12:
        string2 = input("Try to guess the secret number! (4 Characters): ").upper()
        numCorrect = compareStrings(code, string2)

        if numCorrect == -1:
            print("Invalid guess. Please enter 4 characters.")
        elif numCorrect == 4:
            print("Congratulations! You've found the correct code!")
            gameContinue = False
        else:
            incorrectGuesses += 1
            print(f"The number of letters that match is {numCorrect}")
            print(f"You have made {incorrectGuesses} incorrect guesses.")

        continueGame = input("Do you want to continue? (yes/no): ").lower()
        if continueGame == 'no':
            gameContinue = False

    if incorrectGuesses == 12:
        print("You've made 12 incorrect guesses. The secret code was:", code)

main()