# poker_parser.py
'''
This module will parse files into games
'''
import os
import traceback
from game_parser import Parser
from my_utils import find_file
import log
logger = log.get_logger(__name__)

class ParseFile():
    '''
    Given a file name, this can read a file and obtain
    game representation of the games in the file.
    '''

    def __init__(self, file_name):
        self.filedir = find_file(file_name)
        if not self.filedir:
            raise ValueError("Couldn't find file %s" % file_name)
        self.file_lines = open(self.filedir, "r").read()
        self._games = []
        self.data = []

    def split_into_games(self):
        ''' This will split based on 3 newlines as described by data '''
        self.data = self.file_lines.split("\n\n\n")

    def parse_games(self, num=-1):
        ''' parses games into self._games and returns list of Game object '''
        self.split_into_games()

        logger.info("parse_games")
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

    def __init__(self, file_dir_name, ignore=None):
        self.MAX_FILES = 100
        directory = find_file(file_dir_name)
        if os.path.isdir(file_dir_name):
            directory = file_dir_name
        if directory is None:
            raise ValueError("Invalid directory or file")

        self.data = []
        self.files = []
        print(directory)
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                if not ignore or (ignore and not file in ignore):
                    self.data.append(ParseFile(file))
                    self.files.append(file)
                if len(self.files) == self.MAX_FILES:
                    break
        else:
            if not ignore or (ignore and not file_dir_name in ignore):
                self.data = [ParseFile(file_dir_name)]
                self.files = [file_dir_name]
        self._games = []

        logger.info(self.files)

    def parse_games(self, num=-1):
        ''' Parse games from given location '''
        files = []
        for file in self.data:
            try:
                logger.info("Parsing %s", file.filedir)
                data = file.parse_games(num=num)
                self._games.extend(data)
                files.append(file)
            except ValueError as _e:
                logger.info("Error in %s\n%s", file.filedir, repr(_e))
                traceback.print_tb(_e.__traceback__)
            except TypeError as _e:
                logger.info("Error in %s\n%s", file.filedir, repr(_e))
                traceback.print_tb(_e.__traceback__)
            except KeyError as _e:
                logger.info("Error in %s\n%s", file.filedir, repr(_e))
                traceback.print_tb(_e.__traceback__)
            except IndexError as _e:
                logger.info("Error in %s\n%s", file.filedir, repr(_e))
                traceback.print_tb(_e.__traceback__)

        return self._games, self.files

    def games(self):
        ''' Returns games '''
        if not self._games:
            self.parse_games()
        return self._games
