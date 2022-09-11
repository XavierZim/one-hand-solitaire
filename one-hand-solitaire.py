import random as ran
import numpy as np

class deck:
    def __init__(self):
        self.suits = ["Spades","Clubs","Diamonds","Hearts"]
        self.ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.deck = []
        self.hand = []

        self.shuffle()

    #generates and shuffles the deck
    def shuffle(self):
        for i in range(len(self.ranks)):
            for j in range(len(self.suits)):
                self.deck.append((self.ranks[i],self.suits[j]))
        ran.shuffle(self.deck)

    #removes first item from the deck and appends it to the hand
    def draw(self,drawNumber):
        for i in range(drawNumber):
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])

    #sees if there are cards in hand that can be removed and does so according to rules
    def check(self):
        try:
            if self.hand[-1][0] == self.hand[-4][0]:
                del self.hand[-4:]
            elif self.hand[-1][1] == self.hand[-4][1]:
                del self.hand[-3:-2]
            elif len(self.deck) > 0:
                self.draw(1)
        except:
            pass

    #draws appropriate amount of cards if there are not enough
    def drawRule(self):
        self.drawAmount = 4-len(self.hand)
        if self.drawAmount > len(self.deck):
            self.drawAmount = len(self.deck)
        if len(self.hand) < 4 and len(self.deck) > 0:
            self.draw(self.drawAmount)

    #runs an instance of the game
    def run(self):
        while len(self.deck) > 0:
            self.drawRule()
            self.check()

# starts up and plays the number of games specified by user
games = []
for i in range(int(input("number of games to play>"))):
    new = deck()
    new.run()
    games.append(len(new.hand))

# appends the number of won games to a list
wonGames = []
for i in range(len(games)):
    if games[i] == 0:
        wonGames.append(i)

print("0s at:", wonGames)
print("\nchance to get a 0:", str((len(wonGames)/len(games))*100)+"%")
print("mean cards left over:", np.mean(games))
