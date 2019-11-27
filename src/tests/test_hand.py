# test_hand.py
''' This module is for testing hand and card classes '''
from hand import Hand

def test_hand_creation():
    ''' Tests all possible hand prints as well as equality '''
    test = Hand("[Jh Qc]")
    test1 = Hand("[Ac Ts]")
    test2 = Hand("[Ac Ts]")
    test3 = Hand("[As Ts]")
    test4 = Hand("[Ad Ah]")
    assert test != test1 # false
    assert test1 == test2 # true
    assert test1 != test3 # false
    assert test4 != test3 # false
