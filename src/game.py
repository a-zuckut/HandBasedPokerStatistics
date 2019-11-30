# game.py
'''
This module will be a storage facility
'''
import log
logger = log.get_logger(__name__)

class Game():
    '''
        id is game #
        players is dict of players with associated position
        rounds is a list of dict of players with bets
        final is amount players won at end
        settings is settings dictionary
    '''
    def __init__(self, data, settings, showdown=None):
        game_id, players, rounds, final, cards = data

        self._id = game_id # game id (assume unique)
        self._players = players # (id, pos, stack)

        self._bet = {p: 0 for p in players}
        winning = {}
        self._total = {}

        for curr_round, _ in rounds:
            for player in curr_round:
                if not player in self._bet:
                    logger.info("not player in self._bet")
                    logger.info(self._bet)
                    logger.info(curr_round)
                self._bet[player] += curr_round[player]

        self._cards = cards
        self._showdown = showdown

        for player in final:
            winning[player] = final[player] # ($,Hand)
        for player in self._players:
            if player in winning and self._bet:
                self._total[player] = winning[player] - self._bet[player]
            else:
                self._total[player] = - self._bet[player]

        self._settings = settings

    def settings(self):
        ''' Returns the settings as defined in game_parser as well as players '''
        return self._settings, self._players

    def winning_cards(self):
        ''' returns a tuple of showdown cards and total winnings '''
        return self._showdown, self._total

    def __repr__(self):
        return_string = "Game Id: %s; Settings: %s; Total Winnings: %s; Players: %s" % \
            (self._id, self._settings, self._total, self._players)
        if self._showdown:
            return return_string + "; Showdown: " + self._showdown
        return return_string
