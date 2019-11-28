# Hand.py
'''
This handles logic for parsing a Hand and is a container
'''
from card import Card

class Hand():
    '''
    This class takes in two cards ([]) and outputs a list for a hand
    '''
    def __init__(self, given_str, bypass=False):
        given_str = given_str.strip()

        card1 = None
        card2 = None
        if bypass:
            if given_str[-1] == 'o' or given_str[0] == given_str[1]:
                card1 = Card(given_str[0] + 'c')
                card2 = Card(given_str[1] + 's')
            elif given_str[-1] == 's':
                card1 = Card(given_str[0] + 's')
                card2 = Card(given_str[1] + 's')
            else:
                raise TypeError("Not a card %s" % given_str)
        else:
            assert given_str[0] == '[' and given_str[-1] == ']'
            assert len(given_str) >= 7

            if '-' in given_str:
                given_str = given_str.split('-')[0]
            card = given_str[1:-1].split(" ")
            card1 = Card(card[0])
            card2 = Card(card[1])

        if card2 < card1:
            self.hand = [card1, card2]
        else:
            self.hand = [card2, card1]

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        default = self.hand[0].rank + self.hand[1].rank
        if self.hand[0].suit == self.hand[1].suit:
            return default + 's' # suited
        if default[0] == default[1]:
            return default
        return default + 'o' # suited

    def __str__(self):
        default = self.hand[0].rank + self.hand[1].rank
        if self.hand[0].suit == self.hand[1].suit:
            return default + 's' # suited
        if default[0] == default[1]:
            return default
        return default + 'o' # suited

    def __hash__(self):
        return hash(str(self))
