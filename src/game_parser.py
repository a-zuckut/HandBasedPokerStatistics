# GameParser.py
'''
This class will parse the full pokerstar string
'''
import log
from my_utils import parse_info, parse_betting_round, parse_summary, \
                     parse_showdown, fill_in_last_player_to_bet
from game import Game
logger = log.get_logger(__name__)

class Parser():
    '''
    Parser is taking in a gamestr and outputting a data representation of a poker
    hand.
    '''
    def __init__(self, gamestr):
        self._separate = []
        lines = [line for line in gamestr.strip().split('\n') if line]
        temp = []
        for line in lines:
            if '***' in line:
                self._separate.append(temp)
                temp = [line.strip()]
            else:
                temp.append(line.strip())
        if temp:
            self._separate.append(temp)

        if self._separate:
            self.populate()
            self._representation = Game(
                self.data,
                self._settings,
                self._showdown
            )
        else:
            self._representation = None

    def populate(self):
        ''' This method will populate data for this whole function (parsing logic) '''
        self._settings = {}
        self._showdown = None
        _game_id = None
        _players = {}
        _final = {}
        _rounds = []
        self._cards = []

        # init round
        _game_id, _players, settings, round_one = parse_info(self._separate.pop(0))
        _rounds.append(round_one)
        self._settings.update(settings)


        for part in self._separate:
            if "SUMMARY" in part[0]:
                setting, won, cards, hands = parse_summary(part)
                self._settings.update(setting)
                _final = won
                self._cards = cards
                if hands:
                    self._showdown.update(hands)
            elif "SHOW" in part[0] and "DOWN" in part[0]:
                finalist = parse_showdown(part)
                for player in finalist:
                    if player not in _players:
                        finalist = fill_in_last_player_to_bet(_rounds, finalist)
                self._showdown = finalist
            else:
                bets, cards = parse_betting_round(part)
                _rounds.append((bets, cards))

        self.data = (_game_id, _players, _rounds, _final, self._cards)

    def return_game(self):
        ''' This will expose the game representation '''
        return self._representation
