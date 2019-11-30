# profit_per_hand.py
'''
This will obtain parsered data and store data in file
'''
import log
logger = log.get_logger(__name__)

import os
import errno
from poker_parser import ParseDirectory
from hand import Hand

LOCATION = "mydata/profit_per_hand"

def runner(file, save=False):
    '''
    This will run profit per hand on the directory or file given
    '''
    ignored = list()
    data = {}
    if save:
        ignored = get_list_data("ignore.txt")
        data = get_dict_data("hands.txt")

    obtain_data = ParseDirectory(file, ignore=ignored)
    logger.info("Getting data from directory")
    games, files = obtain_data.parse_games()
    logger.info("Getting hands from parsed data")
    hands = get_data(games)
    logger.info("Hands %s" % hands)

    if hands:
        logger.info("updating and storing")
        files = set(files)
        files.update(ignored)

        for values in hands:
            if values in data:
                data[values] = [hands[values][0] + data[values][0],
                                hands[values][1] + data[values][1]]
            else:
                data[values] = hands[values]

        # save data and files that we just ran
        if save:
            store_data(files, "ignore.txt")
            store_data(data, "hands.txt")

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

def get_list_data(filename):
    '''
    Get list data for ignore
    '''
    filename = os.path.join(LOCATION, filename)
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as _file:
            line = _file.readline().replace("\n", "")
            while line:
                data.append(line)
                line = _file.readline()
    else:
        logger.info("Cannot Load file %s" % filename)
    return data

def get_dict_data(filename):
    '''
    Get dict data for profit
    '''
    filename = os.path.join(LOCATION, filename)
    data = {}
    if os.path.exists(filename):
        with open(filename, 'r') as _file:
            line = _file.readline()
            while line:
                key, value = line.split(":")
                profit, number = value.strip().replace("[", "").replace("]", "").split(",")
                data[Hand(key.strip(), bypass=True)] = [float(profit), int(number)]
                line = _file.readline()
    else:
        logger.info("Cannot Load file %s" % filename)
    return data

def store_data(data, filename):
    '''
    Store data based on types
    '''
    filename = os.path.join(LOCATION, filename)
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, 'w') as _file:
        for item in data:
            if isinstance(data, list):
                _file.write(item + "\n")
            elif isinstance(data, dict):
                _file.write(str(item) + ": " + str(data[item]) + "\n")
            elif isinstance(data, set):
                _file.write(item + "\n")
