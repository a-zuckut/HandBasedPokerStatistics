[![Build Status](https://travis-ci.org/a-zuckut/HandBasedPokerStatistics.svg?branch=master)](https://travis-ci.org/a-zuckut/HandBasedPokerStatistics)

# HandBasedPokerStatistics

## Running

#### Functions
ProfitPerHand:

 - To run: ``` python main.py -D src/sample_data -F ProfitPerHand ```
 - Data in ``` mydata/profit_per_hand ```
 - Data Representation by [Big Blinds of Profit, Hands played]



## What Parts

Data is obtained from a obfuscated data source. This is formated like:

```
PokerStars Game #59937795418:  Hold'em No Limit ($3/$6) - 2009/07/01 0:00:01 ET
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
Seat 5: HX/CQJObuMVIi59AV2gnOw collected ($37.05)
```

This means that I need to create a basic parser to parse this kind of data. After that I need to consider how to generalize this data to store it in faster formate to prevent additional reprocessing of data.

Let's phrase some of the data how we want to phrase it post processing. 

For vocabulary:
I will use ```game``` to describe all the actions from people in the game to how much was won with the winning and losing hands.
As mentioned, ```hand``` will describe the 2 cards that each player has. 
Winning will be defined as money you get from a hand, where you have a winning hand as well as the amount you won.
I will want to describe the amount won with respect to big blinds of the game. 
Rake which is the amount the casino keeps for wins will be ignored. 
Hands with no final cards will be tracked, but with respect to amount bet in a certain position associated with a win. 
With amount won with respect to a positional bet, this will also be stored.

### Definition of Queries

#### Hands

For each hand in a game, we want to store the amount that hand won.

Theoretically we want to record more specific data, such as amount won per position and amount of BB won. And what game situation existed. i.e. was there an aggressive player, did they bluff, did they have on average the best hand with respect to the board state?

#### Games

For each game, store how much the winning player won and record the position of that player. Record basic game info including number of players, who the players were, what the stakes were, number of big blinds on the board (or $ (?)), also record how long the game was (i.e. was there a flop, turn, river)

Do we want to include cards?

#### Positional Bets

Which position won the most money. Ignoring all other statistics. Think about ways to include this statistics.



