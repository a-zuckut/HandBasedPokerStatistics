# GameParser.py

import hand

from my_utils import parse_info, parse_betting_round, parse_summary, parse_showdown
from game import Game

# For Pokerstars data
class Parser(object):
    def __init__(self, gamestr):
        self._separate = []
        t = gamestr.split('\n')
        temp = []
        for line in t:
            if '***' in line:
                self._separate.append(temp)
                temp = [line.strip()]
            else:
                temp.append(line.strip())
        self._separate.append(temp)
        self.populate()
        self._representation = Game(
            self._game_id,
            self._players,
            self._rounds,
            self._final,
            self._settings,
            self._cards,
            self._showdown
        )

    def populate(self):
        self._settings = {}
        self._game_id = None
        self._players = {}
        self._final = {}
        self._rounds = []
        self._cards = []
        self._showdown = None

        # init round
        info = self._separate.pop(0)
        self._game_id, self._players, settings, r1 = parse_info(info)
        self._rounds.append(r1)
        self._settings.update(settings)
        
        for part in self._separate:
            if "SUMMARY" in part[0]:
                setting, won, cards = parse_summary(part)
                self._settings.update(setting)
                self._final = won
                self._cards = cards
            elif "SHOW" in part[0] and "DOWN" in part[0]:
                finalist = parse_showdown(part)
                self._showdown = finalist
            else:
                bets, cards = parse_betting_round(part)
                self._rounds.append((bets, cards))

