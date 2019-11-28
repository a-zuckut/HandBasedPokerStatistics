# profit_per_hand.py
'''
This will obtain parsered data and store data in file
'''
import os, errno
from poker_parser import ParseDirectory

LOCATION = "mydata/profit_per_hand"

def runner(file, save=False):
    '''
    This will run profit per hand on the directory or file given
    '''

    obtain_data = ParseDirectory(file)
    games, files = obtain_data.parse_games()
    hands = get_data(games)

    # save data and files that we just ran
    if save:
        store_data(files, "ignore.txt")
        store_data(hands, "hands.txt")

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
                    hand_to_profit[showdown[player]] += total[player]
                else:
                    hand_to_profit[showdown[player]] = total[player]
    return hand_to_profit

def store_data(data, filename):
    filename = os.path.join(LOCATION, filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w') as f:
        for item in data:
            f.write(item)
