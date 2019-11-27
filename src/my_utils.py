# util.py
from card import Card
from hand import Hand

def parse_info(str):
    setting = {}
    game, setting["big_blind"] = get_first_data(str.pop(0))
    round1 = {}
    players = {}
    seats = {}
    num = 0
    for s in str:
        if "button" in s:
            # if we want this logic
            pass
        elif "Seat" in s:
            seat, t = s.split(":")
            seat = num
            num += 1
            player, t = t.split("(", 1)
            player = player.strip()
            t = t.split(" ", 1)[0].replace("$", "").strip()
            players[player] = [None, float(t)] # Pos, $
            seats[player] = seat # for index 0
            seats[seat] = player
        elif "small blind" in s or "big blind" in s:
            player = s.split(":")[0]
            round1[player] = float(s.split("$")[-1])
        else:
            # some incorrect key
            pass

    for player in players:
        if player in round1:
            if round1[player] == setting["big_blind"]:
                players[player][0] = "big_blind"
            else:
                players[player][0] = "SB"

    for player in players:
        if player in round1:
            if round1[player] != setting["big_blind"]:
                size = len(seats) / 2
                small_num = seats[player] - 1
                if small_num < 0:
                    small_num = size - 1
                players[seats[small_num]][0] = "Button"

    boolean = True
    while(boolean):
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
    return game, players, setting, (round1, [])


def get_first_data(str):
    game, str = str.split(":", 1)
    game = game.split('#', 1)[1]

    str, date = str.split("-", 1) # can parse date
    str = str.split('(', 1)[1]
    str = str.split('/')[1]
    str = str.replace('$', "").replace(')', "")
    big_blind = float(str)
    return game, big_blind


def parse_betting_round(str):
    cards = []
    bets = {}
    for line in str:
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

def parse_showdown(str):
    showdown = {} #player: hand
    for line in str:
        if 'shows' in line:
            player, line = line.split(":")
            hand = Hand(line[line.find('['):line.find(']')+1])
            showdown[player] = hand
        else:
            pass
    return showdown

def parse_summary(str):
    v = str.pop(0)
    setting = {}
    won = {}
    cards = []
    for full_string in str:
        if "pot" in full_string or "Rake" in full_string:
            pot, rake = full_string.split("|")
            setting['pot'] = float(pot.split("$")[1].strip())
            setting['rake'] = float(rake.split("$")[1].strip())
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
