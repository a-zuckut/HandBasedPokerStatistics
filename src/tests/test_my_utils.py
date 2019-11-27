# test_my_utils.py

import pytest

from my_utils import getFirstData

@pytest.mark.parametrize("input, game, bigblind", 
	[("PokerStars Game #59940113586:  Hold'em No Limit ($3/$6) - 2009/07/01 0:57:37 ET", '59940113586', 6),
	("PokerStars Game #59940118092:  Hold'em No Limit ($3/$6) - 2009/07/01 0:57:45 ET", '59940118092', 6),
	("PokerStars Game #59940132252:  Hold'em No Limit ($3/$6) - 2009/07/01 0:58:08 ET", '59940132252', 6),
	("PokerStars Game #59968924268:  Hold'em No Limit ($3/$6) - 2009/07/01 13:28:38 ET", '59968924268', 6),
	("PokerStars Game #59937794410:  Hold'em No Limit ($0.10/$0.25) - 2009/07/01 0:00:00 ET", '59937794410', 0.25)
	#("Full Tilt Poker Game #26262271796: Table jYlmZK163oMwAF5lvasQ6w (6 max, deep) - $3/$6 - No Limit Hold'em - 0:00:01 ET - 2009/07/01", 26262271796, 6)
	])
def test_getFirstData(input, game, bigblind):
	test, setting = getFirstData(input)
	assert(test == game and bigblind == setting)