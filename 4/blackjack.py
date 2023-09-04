#challenge is Blackjack, by Al Sweigart al@inventwithpython.com

# Set up the constants:
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.

#define card printing function
def printCard(suit, value):
    valuef, valuel, value = '', '', str(value)
    if len(value) != 2:
        valuef = value + ' '
        valuel = ' ' + value
    else:
        valuef, valuel = value, value
    print(f' ___\n|{valuef} |\n| {suit} |\n| {valuel}|\n ־־־')

printCard(CLUBS, 10)
printCard(CLUBS, 'K')