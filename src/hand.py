# Hand.py

from card import Card

class Hand():
    def __init__(self, str):
        str = str.strip()
        assert str[0] == '[' and str[-1] == ']'
        assert len(str) >= 7

        card = str[1:-1].split(" ")
        card1 = Card(card[0])
        card2 = Card(card[1])

        if card2 < card1:
            self.c = [card1, card2]
        else:
            self.c = [card2, card1]

    def __eq__(self, other):
        return self.c == other.c

    def __repr__(self):
        default = self.c[0].rank + self.c[1].rank
        if self.c[0].suit == self.c[1].suit:
            return default + 's' # suited
        if default[0] == default[1]:
            return default
        return default + 'o' # suited

    def __str__(self):
        default = self.c[0].rank + self.c[1].rank
        if self.c[0].suit == self.c[1].suit:
            return default + 's' # suited
        if default[0] == default[1]:
            return default
        return default + 'o' # suited

