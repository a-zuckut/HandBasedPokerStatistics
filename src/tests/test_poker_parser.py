# test_poker_parser.py
'''
This will test parsing a single file
'''
from poker_parser import ParseFile, ParseDirectory
from profit_per_hand import runner

def test_std_file():
    ''' Testing parsing as described bellow'''
    file_name = "abs NLH handhq_1-OBFUSCATED.txt"
    data = ParseFile(file_name)
    data.parse_games(num=2)

def test_file_in_dir():
    ''' Testing parsing as described bellow'''
    file_name = "abs NLH handhq_1-OBFUSCATED.txt"
    data = ParseDirectory(file_name)
    data.parse_games(num=2)

def test_full_file_in_dir():
    ''' Testing parsing as described bellow'''
    file_name = "abs NLH handhq_1-OBFUSCATED.txt"
    data = ParseDirectory(file_name)
    data.parse_games()

def test_profit_per_hand():
    ''' Testing ProfitPerHand logic '''
    file_name = "abs NLH handhq_1-OBFUSCATED.txt"
    runner(file_name)
