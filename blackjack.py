card_type = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
card_name = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
         pass

class Deck:

    def __init__(self):
        self.deck = []
        for i in card_type:

            for j in card_name:
                self.deck.append(Card(i, j))

    def __repr__(self):
            pass
    def shuffle(self):
            pass
    def deal(self): 
        return Card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self):
        pass
    def adjust_for_ace(self):
        pass


class Chips:
    def init(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        pass

    def lose_bet(self):
        pass



import random


print('Welcome')
chips = int(input('Place your bet: ')) // 20

card1 = random.choice(card_type) + " " + random.choice(card_name) 
card2 = random.choice(card_type) + " " + random.choice(card_name)
if card1 != card2:
    print('Card 1:', card1)
    print('Card 2:', card2)

# else 

# point calculation
# point1 = card1.split(".")[1]
point1 = card_value[card1.split(".")[1]]
point2 = card_value[card2.split(".")[1]]
points = point1 + point2
if points < 21:
    option = int(input('1. Hit or 2. Stand'))