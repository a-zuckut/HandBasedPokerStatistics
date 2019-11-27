# GameParser.py
'''
This class will parse the full pokerstar string
'''
import hand

from my_utils import parse_info, parse_betting_round, parse_summary, parse_showdown
from game import Game

'''
Parser is taking in a gamestr and outputting a data representation of a poker 
hand.
'''
class Parser():
    def __init__(self, gamestr):
        self._separate = []
        lines = gamestr.split('\n')
        temp = []
        for line in lines:
            if '***' in line:
                self._separate.append(temp)
                temp = [line.strip()]
            else:
                temp.append(line.strip())
        self._separate.append(temp)
        self.populate()
        self._representation = Game(
            self.data,
            self._settings,
            self._showdown
        )

    def populate(self):
        self._settings = {}
        _game_id = None
        _players = {}
        _final = {}
        _rounds = []
        _cards = []
        self._showdown = None

        # init round
        info = self._separate.pop(0)
        _game_id, _players, settings, round_one = parse_info(info)
        _rounds.append(round_one)
        self._settings.update(settings)

        for part in self._separate:
            if "SUMMARY" in part[0]:
                setting, won, cards = parse_summary(part)
                self._settings.update(setting)
                _final = won
                _cards = cards
            elif "SHOW" in part[0] and "DOWN" in part[0]:
                finalist = parse_showdown(part)
                self._showdown = finalist
            else:
                bets, cards = parse_betting_round(part)
                _rounds.append((bets, cards))

        self.data = (_game_id, _players, _rounds, _final, _cards)
