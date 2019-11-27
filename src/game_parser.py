# GameParser.py

import hand
from my_utils import parseInfo, parseBettingRound, parseSummary, parseShowdown
from game import Game

# For Pokerstars data
class Parser(object):
    def __init__(self, gamestr):
        self.separate = []
        t = gamestr.split('\n')
        temp = []
        for line in t:
            if '***' in line:
                self.separate.append(temp)
                temp = [line.strip()]
            else:
                temp.append(line.strip())
        self.separate.append(temp)
        self.populate()
        self.representation = Game(
                                self.game_id,
                                self.players,
                                self.rounds,
                                self.final,
                                self.settings,
                                self.cards,
                                self.showdown
                              )

    def populate(self):
        self.settings = {}
        self.game_id = None
        self.players = {}
        self.final = {}
        self.rounds = []
        self.cards = []
        self.showdown = None

        # init round
        info = self.separate.pop(0)
        self.game_id, self.players, settings, r1 = parseInfo(info)
        self.rounds.append(r1)
        self.settings.update(settings)
        
        for part in self.separate:
            if "SUMMARY" in part[0]:
                setting, won, cards = parseSummary(part)
                self.settings.update(setting)
                self.final = won
                self.cards = cards
            elif "SHOW" in part[0] and "DOWN" in part[0]:
                finalist = parseShowdown(part)
                self.showdown = finalist
            else:
                bets, cards = parseBettingRound(part)
                self.rounds.append((bets, cards))

