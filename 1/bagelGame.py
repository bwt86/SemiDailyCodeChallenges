# Objectives: Genherate random number, let user guess number, let user know how correct their guess is, if correct tell user they are correct and ask to play again
#import random for random number generation
import random

def main(): 
    print("Welcome to bagel, the number guessing game!\nPlease guess a 3 digit number and each guess you get a hint to illustrate the correctness of your guess.\nHere are some clues: \nWhat I say and what That means:\n"+
          " Pico: One digit is correct but in the wrong position.\n Fermi: One digit is correct and in the right position.\n Bagels: No digit is correct.\n")
    playGame()
    
def playGame():
    print("I have thought up a number.\nYou have 10 guesses to get it.")
    #generate random number user will be guessing
    randomNumber = generateNumber()
    gotIt = False
    #gamplay loop
    for i in range(10):
        #get input and turn it into a list
        guess = input(f'Guess {i+1}\n')
        guess = list(map(int, list(guess)))
        #if guess not 3 digits, let user know
        if len(guess) != 3 :
            print('Guess should be 3 digits, try again')
        else:
            #if guess is correct then tell user guess is correct and break out
            if guess == randomNumber:
                print("You got it!")
                gotIt = True
                break
            #if guess not correct evaluate if any of the numbers is correct
            else:
                anyNumCorrect = False
                hint = ''
                for i in range(len(guess)):
                    #check if a guessed digit is in the random number
                    if guess[i] in randomNumber:
                        #if number is correct and in right spot then add fermi to output
                        if guess[i] == randomNumber[i]:
                            hint += 'Fermi '
                            anyNumCorrect = True
                        #if number correct but in wrong spot add a pico to output
                        else:
                            hint += 'Pico '
                            anyNumCorrect = True
                #if no numbers correct print bagel
                if not anyNumCorrect:
                    hint += "Bagel"
                print(hint)
    #if user couldnt guess it, say good try and give correct number
    if not gotIt:
        print(f"Good try but the number was {randomNumber[0]}{randomNumber[1]}{randomNumber[2]}")
    #ask to play again
    playAgainQuestion()

#Asks user to play again, if yes then play again and if no or anything else then exit
def playAgainQuestion():
    playAgain = input('Do you want to play again? (yes or no)\n').lower()
    if playAgain == 'yes':
        playGame()
    else:
        print('Thanks for playing!')
        exit()
            

#Generatese random number for user to guess, Will return number as an array of numbers
def generateNumber():
    digits = 3
    number=[]
    for i in range(digits):
        number.append(random.randint(1,9))
    return number

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()