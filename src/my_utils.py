# util.py
'''
This is the util function mainly for parsing data, will have more utility
function in the future to be updated. TODO
'''
import os
from card import Card
from hand import Hand

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
            round1[player] = float(line.split("$")[-1])
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
        if '$' in line and "collected" not in line:
            player, line = line.split(":", 1)
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
        if 'shows' in line:
            player, line = line.split(":")
            hand = Hand(line[line.find('['):line.find(']')+1])
            showdown[player] = hand
        else:
            pass
    return showdown

def parse_summary(given_str):
    ''' This parses the summary screen '''
    _ = given_str.pop(0)
    setting = {}
    won = {}
    cards = []
    for full_string in given_str:
        if "pot" in full_string.lower() and "rake" in full_string.lower():
            pot, rake = full_string.split("|")
            setting['pot'] = float(pot.split("$")[1].strip())
            setting['rake'] = float(rake.split("$")[1].strip())
        elif "pot" in full_string.lower():
            setting['pot'] = float(full_string.split("$")[1].split(")")[0].strip())
        elif "Board" in full_string:
            if '[' in full_string:
                line = full_string.split('[')[-1].replace("]", "")
                cards = [Card(x) for x in line.split(" ")]
        elif "Seat" in full_string:
            if '$' in full_string:
                player, amt = full_string.split(':')[-1].split('$')
                player = full_string.split(" ", 1)[0].strip()
                amt = float(amt.split(")", 1)[0].strip())
                won[player] = amt
        else:
            # something else
            pass
    return setting, won, cards

def find_file(filen):
    '''
    This iterates over current directory looking for file given
    if finds file: returns path; else: return None
    '''
    for dirpath, _, files in os.walk('.'):
        for file in files:
            if file == filen:
                return dirpath + "\\" + file
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
