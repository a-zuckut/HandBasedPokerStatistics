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
    def __init__(self, id, players, rounds, final, settings):
        self.id = id # game id (assume unique)
        self.players = players # (id, pos, stack)

        self.bet = {}
        self.winning = {}
        self.total = {}

        for r, _ in rounds:
            for p in r:
                self.bet[p] += r[p]

        self.cards = [Card(s) for _, s in rounds]

        for p in final:
            self.winning[p] = final[p] # ($,Hand)

        for p,_ in self.players:
            self.total[p] = self.winning[p] - self.bet[p]

        self.bb = settings['big_blind']
        self.rake = settings['rake']
        self.pot = settings['pot']

