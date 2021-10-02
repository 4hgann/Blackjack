from deck import deck
from player import player
import os

def draw(player,freshDeck):
    return player.addCard(freshDeck.draw())

def compare(house,user):
    #Player wins
    if(user.totalValue() > house.totalValue()):
        print('Win!')
    else:
        print('Lose!')

def houseDraw(house,deck):
    print("The house started with: ",end="")
    house.printHand()
    while(house.totalValue() < 17):
        house.addCard(deck.draw())
        print("The house draws and their new hand is: ",end="")
        house.printHand()
    print('The house finishes drawing cards and stays')
    return

def getBuyIn():
    while True:
        try:
            money=input('How much money do you want to cash in? The dealer will begin with twice your amount')
            return int(money)
        except:
            print("That wasn't a valid amount to cash in, try again")

def playRound(house,user):
    freshDeck = deck()
    choice = ""
    #Both house and user start with two cards
    house.addCard(freshDeck.draw())
    house.addCard(freshDeck.draw())
    user.addCard(freshDeck.draw())
    user.addCard(freshDeck.draw())
    

    house.printHand()
    house.printHouse()
    print("Your hand is: ", end="")
    user.printHand()
    choice = input('Do you want to fold (f), draw (d) or stay(s)?')
    while True:

        if(choice == 'd'):
            draw(user,freshDeck)
            print("Your hand is: ", end="")
            user.printHand()
            if user.totalValue() > 21:
                print('Sorry, you went bust!')
                break
        elif(choice == 'f'):
            print('You lost but saved some money')
            break
        else:
            houseDraw(house,freshDeck)
            if(house.totalValue() > 21):
                print('The house went bust, you win!')
                break
            else:
                compare(house,user)
                break
        choice = input('Do you want to fold (f), draw (d) or stay(s)')
    return


if __name__ == "__main__":
    print('Welcome to Henry\'s Blackjack game! Note that the dealer stands on a soft 17')
    money=getBuyIn()
    house = player()
    user = player()

    playRound(house,user)
    while True:

        choice = input('Do you want to play another round? Yes (Y) or No (N)')
        os.system('cls||clear')
        if(choice.lower()=='no' or choice.lower()=='n'):
            break
        elif(choice.lower()=='yes' or choice.lower()=='y'):
            #Reset hands and play another round
            user.resetCards()
            house.resetCards()
            playRound(house,user)
        else:
            print('Fuck you\'re funny, cunt. Enter something right or I\'ll fucking whack you')


    print('Come back another time!')