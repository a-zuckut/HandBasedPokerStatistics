# profit_per_hand.py
'''
This will obtain parsered data and store data in file
'''
from poker_parser import ParseDirectory

LOCATION = "data/profit_per_hand"

def runner(file):
    '''
    This will run profit per hand on the directory or file given
    '''
    obtain_data = ParseDirectory(file)
    games, files = obtain_data.parse_games()
    hands = get_data(games)

    # save data and files that we just ran

    return hands, files

def get_data(games):
    '''
    Games is a list of Game object
    '''
    hand_to_profit = {}
    for game in games:
        showdown, total = game.winning_cards()
        if showdown: # make sure we went to showdown in the first place
            for player in showdown:
                # this is assuming proper syntax
                if showdown[player] in hand_to_profit:
                    hand_to_profit[showdown[player]][0] += total[player] / \
                        game.settings()[0]['big_blind']
                    hand_to_profit[showdown[player]][1] += 1
                else:
                    hand_to_profit[showdown[player]] = [total[player] / \
                        game.settings()[0]['big_blind'], 1]
    return hand_to_profit
