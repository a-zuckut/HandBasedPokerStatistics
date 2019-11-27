# test_hand.py

import pytest
from hand import Hand

def test_hand_creation():
    test = Hand("[Jh Qc]")
    test1 = Hand("[Ac Ts]")
    test2 = Hand("[Ac Ts]")
    test3 = Hand("[As Ts]")
    test4 = Hand("[Ad Ah]")
    assert not (test == test1) # false
    assert (test1 == test2) # true
    assert not (test1 == test3) # false


