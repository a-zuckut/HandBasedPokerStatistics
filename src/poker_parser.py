# poker_parser.py
'''
This module will parse files into games
'''
from game_parser import Parser
from my_utils import find_file

class ParseFile():
    '''
    Given a file name, this can read a file and obtain
    game representation of the games in the file.
    '''

    def __init__(self, file_name):
        filedir = find_file(file_name)
        if not filedir:
            raise ValueError("Couldn't find file %s" % file_name)
        self.file_lines = open(filedir, "r").read()

    def split_into_games(self):
        self.data = self.file_lines.split("\n\n\n")

    def parseGames(self, num=-1):
        self.split_into_games()

        self.games = []
        if num > 0:
            for i in range(num):
                self.games.append(Parser(self.data[i]).return_game())
        else:
            self.games = [Parser(s).return_game() for s in self.data]

        return self.games
