#challenge is Blackjack, by Al Sweigart al@inventwithpython.com
import random

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

def getHandValue(hand):
    val = 0
    for card in hand:
        cardVal = hand[card][1]
        if cardVal in [1,2,3,4,5,6,7,8,9,10]:
            val += cardVal
        else:
            if cardVal in ['J','K','Q']:
                val += 10
            else:
                aceVal = input('You got an Ace! Would you like it to be worth a.) 1 or b.) 11 points\n')
                if aceVal == '1':
                    val += 1
                elif aceVal == '11':
                    val += 11
                else:
                    val += random.choice([1,11])
    return val
def dealCards(hand = {}, qtyToDeal = 1):
    suits = {1: HEARTS, 2: DIAMONDS, 3: SPADES, 4: CLUBS}
    card = [1,2,3,4,5,6,7,8,9,10,'J','K','Q','A']
    for i in range(qtyToDeal):
        hand[len(hand) + 1] = [suits[random.randint(1,4)], random.choice(card)]
    return hand

def displayHand(hand):
    for card in hand:
        printCard(hand[card][0], hand[card][1])

def gameplayLoopPlayer():
    print('Rules:\nTry to get as close to 21 without going over.' +
'Kings, Queens, and Jacks are worth 10 points.\n' +
'Aces are worth 1 or 11 points.\n' +
'Cards 2 through 10 are worth their face value.\n'+
'(H)it to take another card.\n' +
'(S)tand to stop taking cards.')
    playerHand = dealCards(qtyToDeal=2)
    displayHand(playerHand)
    playerHandValue = getHandValue(playerHand)
    print(f"Player Hand with value of {playerHandValue}")
    while playerHandValue < 21:
        choice = input('Do you want to (h)it or (s)tay?\n')
        if choice.lower() == 'h':
            dealCards(qtyToDeal=1)
            displayHand(playerHand)
            playerHandValue = getHandValue(playerHand)
            print(f"Player Hand with value of {playerHandValue}")
        else:
            print(f'You Chose to stay at a hand value of {playerHandValue}')
            break
    if playerHandValue > 21:
        print('You busted!')
    elif playerHandValue == 21:
        print('You got blackjack!')
    
def main():
    gameplayLoopPlayer()

if __name__ == '__main__':
    main()