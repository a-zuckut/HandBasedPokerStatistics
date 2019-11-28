# test_poker_parser.py

from poker_parser import ParseFile

def test_std_file():
	file_name = "abs NLH handhq_1-OBFUSCATED.txt"
	data = ParseFile(file_name)
	games = data.parseGames(num=2)

	print(games)