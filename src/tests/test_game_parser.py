# test_game_parser.py
''' This test tests if the parsing works for the game '''
from game_parser import Parser

def test_simple():
    ''' This test will test a simple no showdown game '''
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
    data = Parser(test).return_game()
    (settings, _) = data.settings()
    assert settings["big_blind"] == 6, "test failed"

def test_showdown():
    ''' This test includes showdown functionality '''
    test = '''PokerStars Game #59937794410:  Hold'em No Limit ($0.10/$0.25) - 2009/07/01 0:00:00 ET
        Table 'vgLbwVmy1dOb81ICg4y5+Q' 6-max Seat #6 is the button
        Seat 2: vjkMgvG+N1YrdituSQFzbQ ($25 in chips) 
        Seat 4: C79eKghuAVSmzDgIazSFCg ($54.75 in chips) 
        Seat 5: 32YL2ZEp8NT4JB2RVM9euQ ($16.35 in chips) 
        Seat 6: xRkU4+naLuz7dEZFbOn9cw ($24.65 in chips) 
        vjkMgvG+N1YrdituSQFzbQ: posts small blind $0.10
        C79eKghuAVSmzDgIazSFCg: posts big blind $0.25
        *** HOLE CARDS ***
        32YL2ZEp8NT4JB2RVM9euQ: folds 
        xRkU4+naLuz7dEZFbOn9cw: raises $0.50 to $0.75
        vjkMgvG+N1YrdituSQFzbQ: folds 
        C79eKghuAVSmzDgIazSFCg: calls $0.50
        *** FLOP *** [4d Qs 4s]
        C79eKghuAVSmzDgIazSFCg: checks 
        xRkU4+naLuz7dEZFbOn9cw: checks 
        *** TURN *** [4d Qs 4s] [9h]
        C79eKghuAVSmzDgIazSFCg: checks 
        xRkU4+naLuz7dEZFbOn9cw: checks 
        *** RIVER *** [4d Qs 4s 9h] [Ad]
        C79eKghuAVSmzDgIazSFCg: checks 
        xRkU4+naLuz7dEZFbOn9cw: checks 
        *** SHOW DOWN ***
        C79eKghuAVSmzDgIazSFCg: shows [8s Ah] (two pair, Aces and Fours)
        xRkU4+naLuz7dEZFbOn9cw: mucks hand 
        C79eKghuAVSmzDgIazSFCg collected $1.55 from pot
        *** SUMMARY ***
        Total pot $1.60 | Rake $0.05 
        Board [4d Qs 4s 9h Ad]
        Seat 2: vjkMgvG+N1YrdituSQFzbQ (small blind) folded before Flop
        Seat 4: C79eKghuAVSmzDgIazSFCg (big blind) showed [8s Ah] and won ($1.55) with two pair, Aces and Fours
        Seat 5: 32YL2ZEp8NT4JB2RVM9euQ folded before Flop (didn't bet)
        Seat 6: xRkU4+naLuz7dEZFbOn9cw (button) mucked'''
    data = Parser(test).return_game()
    settings, _ = data.settings()
    assert settings["big_blind"] == 0.25, "test failed"

def test_more_functionality():
    ''' This test tests more functionality '''
    test = '''Stage #3017235114: Holdem  No Limit $0.50 - 2009-07-01 00:00:01 (ET)
        Table: DEFIANCE ST (Real Money) Seat #6 is the dealer
        Seat 6 - C71mm6MhFIxjPW1vaAXL1g ($55.30 in chips)
        Seat 2 - Qt5Yyd/Y121jtIk37c7TSg ($12.82 in chips)
        Seat 3 - l1bCLGuFqeFRwUfPsiDu/g ($147.69 in chips)
        Seat 4 - 13/ez0NPA4uRcBJ1Rafl6A ($17.90 in chips)
        Seat 5 - TmKBFDTMzV3f+C/n1iWjGQ ($46.04 in chips)
        Qt5Yyd/Y121jtIk37c7TSg - Posts small blind $0.25
        l1bCLGuFqeFRwUfPsiDu/g - Posts big blind $0.50
        *** POCKET CARDS ***
        13/ez0NPA4uRcBJ1Rafl6A - Folds
        TmKBFDTMzV3f+C/n1iWjGQ - Folds
        C71mm6MhFIxjPW1vaAXL1g - Folds
        Qt5Yyd/Y121jtIk37c7TSg - Folds
        *** SHOW DOWN ***
        l1bCLGuFqeFRwUfPsiDu/g - Does not show
        l1bCLGuFqeFRwUfPsiDu/g Collects $0.75 from main pot
        *** SUMMARY ***
        Total Pot($0.75)
        Seat 2: Qt5Yyd/Y121jtIk37c7TSg (small blind) Folded on the POCKET CARDS
        Seat 3: l1bCLGuFqeFRwUfPsiDu/g (big blind) collected Total ($0.75)
        Seat 4: 13/ez0NPA4uRcBJ1Rafl6A Folded on the POCKET CARDS
        Seat 5: TmKBFDTMzV3f+C/n1iWjGQ Folded on the POCKET CARDS
        Seat 6: C71mm6MhFIxjPW1vaAXL1g (dealer) Folded on the POCKET CARDS'''
    data = Parser(test).return_game()
    settings, _ = data.settings()
    assert settings["big_blind"] == 0.50, "test failed"

    test = '''Stage #3017237934: Holdem (1 on 1)  No Limit $0.50 - 2009-07-01 00:00:03 (ET)
        Table: GERMANY HWY (Real Money) Seat #4 is the dealer
        Seat 4 - QiLz8xreFvpFCuxIwseb6A ($14.07 in chips)
        Seat 6 - t4Nq3sihzEUy18XoQoIY9w ($89.54 in chips)
        QiLz8xreFvpFCuxIwseb6A - Posts small blind $0.25
        t4Nq3sihzEUy18XoQoIY9w - Posts big blind $0.50
        *** POCKET CARDS ***
        QiLz8xreFvpFCuxIwseb6A - Folds
        *** SHOW DOWN ***
        t4Nq3sihzEUy18XoQoIY9w - Does not show
        t4Nq3sihzEUy18XoQoIY9w Collects $0.75 from main pot
        *** SUMMARY ***
        Total Pot($0.75)
        Seat 4: QiLz8xreFvpFCuxIwseb6A (dealer) (small blind) Folded on the POCKET CARDS
        Seat 6: t4Nq3sihzEUy18XoQoIY9w (big blind) collected Total ($0.75)'''
    data = Parser(test).return_game()
    settings, _ = data.settings()
    assert settings["big_blind"] == 0.50, "test failed"
