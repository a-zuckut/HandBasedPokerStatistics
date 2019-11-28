# test_poker_parser.py
'''
This will test parsing a single file
'''
from poker_parser import ParseFile

def test_std_file():
    ''' Testing parsing as described bellow'''
    file_name = "abs NLH handhq_1-OBFUSCATED.txt"
    data = ParseFile(file_name)
    games = data.parse_games(num=2)

    print(games)
