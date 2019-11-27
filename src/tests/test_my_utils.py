# test_my_utils.py
''' This module will test my_utils.py '''
import pytest

from my_utils import get_first_data

@pytest.mark.parametrize("input_data, game, bigblind", [
        ("PokerStars Game #59940113586:  Hold'em No Limit ($3/$6) - 2009/07/01 0:57:37 ET",
         '59940113586', 6),
        ("PokerStars Game #59940118092:  Hold'em No Limit ($3/$6) - 2009/07/01 0:57:45 ET",
         '59940118092', 6),
        ("PokerStars Game #59940132252:  Hold'em No Limit ($3/$6) - 2009/07/01 0:58:08 ET",
         '59940132252', 6),
        ("PokerStars Game #59968924268:  Hold'em No Limit ($3/$6) - 2009/07/01 13:28:38 ET",
         '59968924268', 6),
        ("PokerStars Game #59937794410:  Hold'em No Limit ($0.10/$0.25) - 2009/07/01 0:00:00 ET",
         '59937794410', 0.25)
])
def test_get_first_data(input_data, game, bigblind):
    ''' Parameterized test for get_first_data function '''
    test, setting = get_first_data(input_data)
    assert(test == game and bigblind == setting)
