# util.py
from card import Card
from hand import Hand

def parseInfo(str):
    setting = {}
    game, setting["big_blind"] = getFirstData(str.pop(0))
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

    for p in players:
        if p in round1:
            if round1[p] == setting["big_blind"]:
                players[p][0] = "BB"
            else:
                players[p][0] = "SB"

    for p in players:
        if p in round1:
            if round1[p] != setting["big_blind"]:
                size = len(seats) / 2
                sn = seats[p] - 1
                if sn < 0:
                    sn = size - 1
                players[seats[sn]][0] = "Button"

    b = True
    while(b):
        for p in players:
            if players[p][0] is None:
                lindex = seats[p] + 1
                rindex = seats[p] - 1
                if lindex == len(seats) / 2:
                    lindex = 0
                if rindex < 0:
                    rindex = len(seats) / 2 - 1

                left = players[seats[lindex]][0]
                right = players[seats[rindex]][0]
                if right:
                    if right == "BB":
                        players[p][0] = "UTG"
                        continue
                if left:
                    if left == "Button":
                        players[p][0] = "Cut-Off"
                    elif left == "Cut-Off" or "Middle-Position":
                        players[p][0] = "Middle-Position"

        b = False
        for p in players:
            if not players[p][0]:
                b = True
                break
    return game, players, setting, (round1, [])


def getFirstData(str):
    game, str = str.split(":", 1)
    game = game.split('#', 1)[1]

    str, date = str.split("-", 1) # can parse date
    str = str.split('(', 1)[1]
    str = str.split('/')[1]
    str = str.replace('$', "").replace(')', "")
    bb = float(str)
    return game, bb


def parseBettingRound(str):
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

def parseShowdown(str):
    showdown = {} #player: hand
    for line in str:
        if 'shows' in line:
            player, line = line.split(":")
            hand = Hand(line[line.find('['):line.find(']')+1])
            showdown[player] = hand
        else:
            pass
    return showdown

def parseSummary(str):
    v = str.pop(0)
    setting = {}
    won = {}
    cards = []
    for s in str:
        if "pot" in s or "Rake" in s:
            pot, rake = s.split("|")
            setting['pot'] = float(pot.split("$")[1].strip())
            setting['rake'] = float(rake.split("$")[1].strip())
        elif "Board" in s:
            if '[' in s:
                line = s.split('[')[-1].replace("]", "")
                cards = [Card(x) for x in line.split(" ")]
        elif "Seat" in s:
            if '$' in s:
                player, amt = s.split(':')[-1].split('$')
                player = s.split(" ", 1)[0].strip()
                amt = float(amt.split(")", 1)[0].strip())
                won[player] = amt
        else:
            # something else
            pass
    return setting, won, cards

