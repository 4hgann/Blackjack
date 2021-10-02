from deck import deck
from player import player

def draw(player,freshDeck):
    return player.addCard(freshDeck.draw())

def compare(house,user):
    #Player wins
    if(user.totalValue() > house.totalValue()):
        print('Win!')
    else:
        print('Lose!')


def playRound(house,user):
    freshDeck = deck()
    choice = ""
    #Both house and user start with two cards
    house.addCard(freshDeck.draw())
    house.addCard(freshDeck.draw())
    user.addCard(freshDeck.draw())
    user.addCard(freshDeck.draw())
    
    user.printHand()
    house.printHand()
    house.printHouse()
    choice = input('Do you want to fold (f), draw (d) or stay(s)?')
    while(True):

        if(choice == 'd'):
            draw(user,freshDeck)
        elif(choice == 'f'):
            print('You lost but saved some money')
            break
        else:
            compare(house,user)
            break

        choice = input('Do you want to fold (f), draw (d) or stay(s)')
    return


if __name__ == "__main__":
    print('Welcome to Henry\'s Blackjack game!')
    house = player([])
    user = player([])
    playRound(house,user)
    print('Good round!')