# Card.py
'''
This Module will carry all the logic and ordering behind the cards themselves
'''
class Card():
    '''
      Given the implementation of data given, we will parse in this manner
    '''
    def __init__(self, given_str):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', '10', \
            'J', 'Q', 'K', 'A']
        self.suits = ['c', 's', 'h', 'd']

        given_str = given_str.strip() # remove all whitespace
        assert len(given_str) <= 3 and len(given_str) >= 2
        rank = given_str[0]
        if rank == '1' and given_str[:-1] in self.ranks and len(given_str) == 3:
            rank = 'T'
        suit = given_str[-1]
        assert suit in self.suits
        assert rank in self.ranks

        self.rank = rank
        self.suit = suit

        assert self.rank
        assert self.suit

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank)

    def __gt__(self, other):
        return self.ranks.index(self.rank) > self.ranks.index(other.rank)
