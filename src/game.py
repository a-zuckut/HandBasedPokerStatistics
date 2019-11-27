# game.py

from hand import Hand
from card import Card

class Game(object):

    '''
        id is game #
        players is dict of players with associated position
        rounds is a list of dict of players with bets
        final is amount players won at end
        settings is settings dictionary
    '''

    def __init__(self, id, players, rounds, final, settings, cards, showdown=None):
        self._id = id # game id (assume unique)
        self._players = players # (id, pos, stack)

        self._bet = {p: 0 for p in players}
        self._winning = {}
        self._total = {}

        for r, _ in rounds:
            for p in r:
                self._bet[p] += r[p]

        self._cards = cards
        self._showdown = showdown

        for p in final:
            self._winning[p] = final[p] # ($,Hand)

        for p in self._players:
            if p in self._winning and self._bet:
                self._total[p] = self._winning[p] - self._bet[p]
        self.bb = settings['big_blind']
        self.rake = settings['rake']
        self.pot = settings['pot']
