# test_game_parser.py

import pytest
from game_parser import Parser

def test_simple():
    test = '''PokerStars Game #59937795418:  Hold'em No Limit ($3/$6) - 2009/07/01 0:00:01 ET
                Table 'eZ9obi4Bm6uzF08iPplRdg' 6-max Seat #1 is the button
                Seat 1: ZqHBrNHc6FV5pubHfOX06w ($570 in chips)
                Seat 2: 7u7CVWLfH5mxzeWdRgWV4Q ($114 in chips)
                Seat 3: DWBdVLk+3qim/Ax0BIC30A ($384.40 in chips)
                Seat 4: kem0o3a/3AcDZBJg3cdvpQ ($123.50 in chips)
                Seat 5: HX/CQJObuMVIi59AV2gnOw ($1819.70 in chips)
                7u7CVWLfH5mxzeWdRgWV4Q: posts small blind $3
                DWBdVLk+3qim/Ax0BIC30A: posts big blind $6
                *** HOLE CARDS ***
                kem0o3a/3AcDZBJg3cdvpQ: folds
                HX/CQJObuMVIi59AV2gnOw: raises $12 to $18
                UeVOmzLX2mAh84TEAZpMSg joins the table at seat #6
                ZqHBrNHc6FV5pubHfOX06w: folds
                7u7CVWLfH5mxzeWdRgWV4Q: folds
                DWBdVLk+3qim/Ax0BIC30A: calls $12
                *** FLOP *** [8s Jh 8c]
                DWBdVLk+3qim/Ax0BIC30A: checks
                HX/CQJObuMVIi59AV2gnOw: bets $24
                DWBdVLk+3qim/Ax0BIC30A: folds
                HX/CQJObuMVIi59AV2gnOw collected $37.05 from pot
                HX/CQJObuMVIi59AV2gnOw: doesn't show hand
                *** SUMMARY ***
                Total pot $39 | Rake $1.95
                Board [8s Jh 8c]
                Seat 1: ZqHBrNHc6FV5pubHfOX06w (button) folded before Flop (didn't bet)
                Seat 2: 7u7CVWLfH5mxzeWdRgWV4Q (small blind) folded before Flop
                Seat 3: DWBdVLk+3qim/Ax0BIC30A (big blind) folded on the Flop
                Seat 4: kem0o3a/3AcDZBJg3cdvpQ folded before Flop (didn't bet)
                Seat 5: HX/CQJObuMVIi59AV2gnOw collected ($37.05)'''
    Parser(test)
