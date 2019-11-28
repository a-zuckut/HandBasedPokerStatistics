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
        self.games = []
        self.data = []

    def split_into_games(self):
        ''' This will split based on 3 newlines as described by data '''
        self.data = self.file_lines.split("\n\n\n")

    def parse_games(self, num=-1):
        ''' parses games into self.games and returns list of Game object '''
        self.split_into_games()

        if num > 0:
            for i in range(num):
                self.games.append(Parser(self.data[i]).return_game())
        else:
            self.games = [Parser(s).return_game() for s in self.data]

        return self.games
