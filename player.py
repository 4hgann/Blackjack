from card import *

class player:
    def __init__(self,cards):
        self.cards = cards

    def totalValue(self):
        value=0
        for i in range(len(self.cards)):
            value+=self.cards[i].value
        
        return value
    
    def addCard(self, card):
        self.cards.append(card)
        return

    def printValue(self, cardValue):
            if cardValue == 1:
                print("Ace", end="")
            elif cardValue == 11:
                print("Jack", end="")
            elif cardValue == 12:
                print("Queen", end="")
            elif cardValue == 13:
                print("King", end="")
            else:
                print(str(cardValue),end="")

    def printSuit(self, suit):
        if(suit==1):
            print("Spades",end="")
        elif(suit==2):
            print("Hearts",end="")
        elif(suit==3):
            print("Clubs",end="")
        else:
            print("Diamonds",end="")

    #Format of printing is "Your hand is: Ace of Spades and 10 of hearts"
    def printHand(self):
        print("Your hand is: ", end="")
        for i in range(len(self.cards)):
            if(i == len(self.cards)-1 and i != 0):
                print(" & ",end="")
            elif(i > 0):
                print(", ",end="")

            self.printValue(self.cards[i].value)
            print(" of ",end="")
            self.printSuit(self.cards[i].suit)

        print("")
        return
    
    def printHouse(self):
        print("The house has a: ", end="")
        self.printValue(self.cards[0].value)
        print(" of ", end="")
        self.printSuit(self.cards[0].suit)
        print(" . Their other card is hidden!")
    
