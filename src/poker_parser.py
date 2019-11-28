# poker_parser.py
'''
This module will parse files into games
'''
import os
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
        self._games = []
        self.data = []

    def split_into_games(self):
        ''' This will split based on 3 newlines as described by data '''
        self.data = self.file_lines.split("\n\n\n")

    def parse_games(self, num=-1):
        ''' parses games into self._games and returns list of Game object '''
        self.split_into_games()

        if num > 0:
            for i in range(num):
                self._games.append(Parser(self.data[i]).return_game())
        else:
            self._games = [Parser(s).return_game() for s in self.data if Parser(s).return_game()]

        return self._games

class ParseDirectory():
    '''
    Either parses a given directory or file
    '''

    def __init__(self, file_dir_name, ignore=[]):
        directory = find_file(file_dir_name)
        if os.path.isdir(file_dir_name):
            directory = file_dir_name
        if directory == None:
            raise ValueError("Invalid directory or file")

        if os.path.isdir(directory):
            self.data = []
            self.files = []
            print("directory")
            for file in os.listdir(directory):
                if not file in ignore:
                    self.data.append(ParseFile(file))
        else:
            self.data = [ParseFile(file_dir_name)]
            self.files = [file_dir_name]
        self._games = []

    def parse_games(self, num=-1):
        ''' Parse games from given location '''
        for file in self.data:
            try:
                self._games.extend(file.parse_games(num=num))
            except Error as e:
                print("Error in %s, %s" % (file, e))
        return self._games, self.files

    def games(self):
        ''' Returns games '''
        if not self._games:
            self.parse_games()
        return self._games
