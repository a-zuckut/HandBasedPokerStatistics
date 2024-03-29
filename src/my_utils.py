# util.py
'''
This is the util function mainly for parsing data, will have more utility
function in the future to be updated. TODO
'''
import os
import re
from card import Card
from hand import Hand
import log
logger = log.get_logger(__name__)


def parse_info(given_str):
    '''
    Parse info will parse the initial parts of the poker game
    '''
    setting = {}
    game, setting["big_blind"] = get_first_data(given_str.pop(0))
    round1 = {}
    players = {}
    seats = {}
    num = 0
    for line in given_str:
        if "button" in line or "dealer" in line:
            # if we want this logic
            pass
        elif "Seat" in line:
            split = ":"
            if count_occurrences(line, split) < 1:
                split = "-"
            seat, temp = line.split(split)
            seat = num
            num += 1
            player, temp = temp.split("(", 1)
            player = player.strip()
            temp = temp.split(" ", 1)[0].replace("$", "").strip()
            players[player] = [None, float(temp)] # Pos, $
            seats[player] = seat # for index 0
            seats[seat] = player
        elif "small blind" in line or "big blind" in line:
            split = ":"
            if count_occurrences(line, split) < 1:
                split = "-"
            player = line.split(split)[0].strip()
            if "$" in line:
                round1[player.strip()] = float(line.split("$")[-1])
            if player not in players:
                players[player] = [None, float(setting['big_blind']*100)]
                seat = num
                num += 1
                seats[player] = seat
                seats[seat] = player
        else:
            # some incorrect key
            pass

    fill_first_seats(players, round1, setting, seats)
    fill_complex_seats(players, seats)

    return game, players, setting, (round1, [])

def fill_first_seats(players, round1, setting, seats):
    ''' fils BB SB Button '''
    for player in players:
        if player in round1:
            if round1[player] == setting["big_blind"]:
                players[player][0] = "Big Blind"
            else:
                players[player][0] = "Small Blind"

    for player in players:
        if player in round1:
            if round1[player] != setting["big_blind"]:
                size = len(seats) / 2
                small_num = seats[player] - 1
                if small_num < 0:
                    small_num = size - 1
                players[seats[small_num]][0] = "Button"

def fill_complex_seats(players, seats):
    ''' fills UTG, MP, etc '''
    boolean = True
    while boolean:
        for player in players:
            if players[player][0] is None:
                lindex = seats[player] + 1
                rindex = seats[player] - 1
                if lindex == len(seats) / 2:
                    lindex = 0
                if rindex < 0:
                    rindex = len(seats) / 2 - 1

                left = players[seats[lindex]][0]
                right = players[seats[rindex]][0]
                if right:
                    if right == "big_blind":
                        players[player][0] = "UTG"
                        continue
                if left:
                    if left == "Button":
                        players[player][0] = "Cut-Off"
                    elif left == "Cut-Off" or "Middle-Position":
                        players[player][0] = "Middle-Position"

        boolean = False
        for player in players:
            if not players[player][0]:
                boolean = True
                break

def get_first_data(given_str):
    ''' This method will get the first pieces of data for the game '''
    game, given_str = given_str.split(":", 1)
    game = game.split('#', 1)[1]

    given_str, _ = given_str.split("-", 1) # can parse date
    if count_occurrences(given_str, '$') == 2:
        given_str = given_str.split('(', 1)[1]
        given_str = given_str.split('/')[1]
        given_str = given_str.replace('$', "").replace(')', "")
        big_blind = float(given_str)
        return game, big_blind
    if count_occurrences(given_str, '$') == 1:
        big_blind = float(given_str.split('$', 1)[1].split(" ")[0].strip())
        return game, big_blind

    raise Exception("We don't have any money?")

def parse_betting_round(given_str):
    ''' This parses each betting round generically '''
    cards = []
    bets = {}
    for line in given_str:
        if '$' in line and "collected" not in line and "returned" not in line:
            split = ":"
            if count_occurrences(line, split) < 1:
                split = "-"
            player, line = line.split(split, 1)
            if "raises" in line:
                bets[player.strip()] = float(line.split("$")[-1].split(" ")[0])
            else:
                bets[player.strip()] = float(line.split("$")[-1])
        elif '***' in line:
            if '[' in line:
                line = line.split('[')[-1].replace("]", "")
                cards = [Card(s) for s in line.split(" ")]
        else:
            # something that we don't want to track
            pass

    return bets, cards

def parse_showdown(given_str):
    ''' This parses the showdown screen '''
    showdown = {} #player: hand
    for line in given_str:
        if 'shows' in line.lower():
            split = ":"
            if count_occurrences(line, split) < 1:
                split = "-"
            player, line = line.split(split)
            hand = Hand(line[line.find('['):line.find(']')+1])
            showdown[player.strip()] = hand
        elif 'muck' in line.lower():
            split = ":"
            if count_occurrences(line, split) < 1:
                split = "-"
            player, line = line.split(split)
            line = line.lower().split("muck")[-1]
            line = line[line.find('['):line.find(']')+1]
            if line:
                hand = Hand(line)
                showdown[player.strip()] = hand
        else:
            pass
    return showdown

def parse_summary(given_str):
    ''' This parses the summary screen '''
    _ = given_str.pop(0)
    setting = {}
    won = {}
    cards = []
    showdown = {}
    for full_string in given_str:
        if "pot" in full_string.lower() and "rake" in full_string.lower():
            pot, rake = full_string.split("|", 1)
            setting['pot'] = float(re.sub("[^[0-9.]", "",
                                          pot.split("$")[1].split(")")[0].strip()))
            setting['rake'] = float(re.sub("[^[0-9.]", "",
                                           rake.split("$")[1].split(")")[0].strip()))
        elif "Pot" in full_string or "pot" in full_string:
            setting['pot'] = float(full_string.split("$")[1].split(")")[0].strip())
        elif "Board" in full_string:
            if '[' in full_string:
                line = full_string.split('[')[-1].replace("]", "")
                cards = [Card(x) for x in line.split(" ")]
        elif "Seat" in full_string:
            if '$' in full_string:
                split = ":"
                if count_occurrences(full_string, split) < 1:
                    split = "-"
                player, amt = full_string.split(split)[1].split('$')
                player = player.strip().split(" ", 1)[0]
                amt = float(amt.split(")", 1)[0].strip())
                won[player.strip()] = amt
            elif 'muck' in full_string.lower():
                split = ":"
                if count_occurrences(full_string, split) < 1:
                    split = "-"
                try:
                    _, full_string = full_string.split(split, 1)
                    player = full_string.strip().split(" ")[0]
                    full_string = full_string.lower().split("muck")[-1]
                    full_string = full_string[full_string.find('['):
                                              full_string.find(']', full_string.find('['))+1]
                    if full_string:
                        hand = Hand(full_string)
                        showdown[player.strip()] = hand
                except ValueError:
                    continue
    return setting, won, cards, showdown

def find_file(filen):
    '''
    This iterates over current directory looking for file given
    if finds file: returns path; else: return None
    '''
    for dirpath, _, files in os.walk('.'):
        for file in files:
            if file == filen:
                return os.path.join(dirpath, file)
    return None

def count_occurrences(test_str, _ch):
    '''
    Method that counts the number of occurrences of c in test_str
    '''
    count = 0
    for i in test_str:
        if i == _ch:
            count += 1
    return count

def fill_in_last_player_to_bet(rounds, finalist):
    '''
    This takes in the rounds and a broken finalist dict and fixes finalists
    '''
    comparison = finalist
    last_round = None
    for curr_round in reversed(rounds):
        player_list = curr_round[0]
        if player_list:
            last_round = list(player_list.keys())
            break
    return_value = {}
    key = None
    value = None
    for player in last_round:
        if not player in comparison:
            key = player
        else:
            return_value[player] = finalist[player]
    for player in comparison:
        if not player in return_value:
            value = finalist[player]
    if key and value:
        return_value[key] = value
    return return_value
