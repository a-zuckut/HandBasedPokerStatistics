# Card.py

class Card (object):
  '''
    Given the implementation of data given, we will parse in this manner
  '''
  def __init__ (self, str):
    self.RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', \
        'J', 'Q', 'K', 'A']
    self.SUITS = ['c', 's', 'h', 'd']


    str = str.strip() # remove all whitespace
    assert len(str) <= 3 and len(str) >= 2
    rank = str[0]
    suit = str[-1]
    assert(suit in self.SUITS)
    assert(rank in self.RANKS)

    self.rank = rank
    self.suit = suit

    assert self.rank
    assert self.suit

  def rank(self):
      return self.rank

  def suit(self):
      return self.suit

  def __str__ (self):
    return self.rank + self.suit

  def __repr__(self):
    return self.rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank) and \
           (self.suit == other.suit)

  def __lt__ (self, other):
    return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

  def __gt__ (self, other):
    return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

