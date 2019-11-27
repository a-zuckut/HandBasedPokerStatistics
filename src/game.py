# game.py

class Game():
    '''
        id is game #
        players is dict of players with associated position
        rounds is a list of dict of players with bets
        final is amount players won at end
        settings is settings dictionary
    '''
    def __init__(self, data, settings, showdown=None):
        id, players, rounds, final, cards = data

        self._id = id # game id (assume unique)
        self._players = players # (id, pos, stack)

        self._bet = {p: 0 for p in players}
        winning = {}
        self._total = {}

        for r, _ in rounds:
            for p in r:
                self._bet[p] += r[p]

        self._cards = cards
        self._showdown = showdown

        for p in final:
            winning[p] = final[p] # ($,Hand)

        for p in self._players:
            if p in winning and self._bet:
                self._total[p] = winning[p] - self._bet[p]

        self.settings = settings

    def settings():
        return self.settings

    def winningCards():
        return self._showdown, self._total
