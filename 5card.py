'''
To Do:
-Score hands
-Add betting results

Advanced:
-allow computer to replace hand, probably won't be able to do this for awhile
'''


import random
import re
deck = list()
myhand=list()
comphand=list()
mscore=0
cscore=0
wallet=50

def builddeck(suit):
    #instructions to build deck so you don't have to type in all 52 cards
    #will additionally use to "shuffle" the deck after each round
    card =2
    while card <11:
        card = str(card)
        newcard =(card + suit)
        deck.append(newcard)
        card = int(card)
        card=card +1
    deck.append('J' + suit)
    deck.append('Q' + suit)
    deck.append('K' + suit)
    deck.append('A' + suit)



def drawhand():

    if wallet <0:
        print("You are out of money, it's time to go home")
        exit()
    while wallet >1000:
        print("You've made over $1000, know how to quit while you're ahead!")
        exit()
    #run deckbuilder in here to "reshuffle" every round
    builddeck(' ♦')
    builddeck(' ♠')
    builddeck(' ♥')
    builddeck(' ♣')
    #instructions to draw hands for player and computer
    bet=input('How much would you like to bet? Answer in whole dollars, you currently have %d dollars, must bet at least 1 dollar ' % wallet)
    try:
        int(bet)
    #don't remember how to get except statement to repeat (turn into a function and use recursion?)
    except:
        print("Invalid input, try again, whole numbers only")
        bet=input('How much would you like to bet? Answer in whole dollars, you currently have %d dollars, must bet at least 1 dollar ' % wallet)

    myhand.clear()
    comphand.clear()
    for i in range(5):
        mc1=random.choice(deck)
        deck.remove(mc1)
        myhand.append(mc1)
        cc1=random.choice(deck)
        deck.remove(cc1)
        comphand.append(cc1)

    print("Your cards are:",myhand)
    trade=input("\nWould you like to trade any cards? y/n: ")
    if trade == "y" or redraw =="Y":
        redraw()

    anothergame=input("Play again? Y/N: ")
    if anothergame == 'Y' or anothergame == 'y':
        deck.clear()
        drawhand()

def redraw():
    i=0
    while i<5:
        print("Would you like to exchange card:",myhand[i])
        exchange=input(" y/n: ")
        if exchange == 'y' or exchange == "y":
            myhand.pop(i)
            new=random.choice(deck)
            #note, if you append instead of insert, it adds to end of list and messes up the count
            myhand.insert(i, new)
            deck.remove(new)
        i=i+1
    print("new hand is:",myhand)

#def scorehand(hand):
    #need to score Royal flush, straight flush, four of a kind, full house, flush, straight , 3 of a kind, 2 pairs, 1 pair, high card
    #for card in hand:


drawhand()
