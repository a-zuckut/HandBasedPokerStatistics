# GameParser.py

import hand
from my_utils import parseInfo, parseBettingRound

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

        self.populate()

    def populate(self):
        self.settings = {}
        self.game_id = None
        self.players = {}
        self.final = {}
        self.rounds = []

        # init round
        info = self.separate.pop(0)
        self.game_id, self.players, settings, r1 = parseInfo(info)
        self.rounds.append(r1)
        self.settings.update(settings)
        
        for part in self.separate:
            if "SUMMARY" in part:
                parseSummary(part)
            elif "SHOW" in part and "DOWN" in part:
                parseShowdown(part)
            else:
                bets, cards = parseBettingRound(part)
                self.rounds.append((bets, cards))





