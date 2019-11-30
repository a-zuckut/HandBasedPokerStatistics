# visualize.py

import os
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from hand import Hand
import log
logger = log.get_logger(__name__)

DIRECTORY = 'mydata'

def visualize(function, data):
    if function.lower() == "profitperhand":
        table = construct_order()
        create_heatmap(table, data, function)
    else:
        logger.info("Visualization Not Supported for %s", function)

def construct_order():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', \
                'J', 'Q', 'K', 'A']
    ranks.reverse()
    table = []
    for col, _ in enumerate(ranks):
        temp = []
        for row, _ in enumerate(ranks):
            cards = ranks[col] + ranks[row]
            if col < row:
                cards += 's'
            elif col > row:
                cards += 'o'
            temp.append(Hand(cards, bypass=True))
        table.append(temp)
    return table

def create_heatmap(labels, data, file_name):
    data_for_numpy = []
    labels_for_numpy = []
    for row in labels:
        temp = []
        temp2 = []
        for hand in row:
            temp.append(round(data[hand][0] / data[hand][1], 2))
            temp2.append(str(hand))
        data_for_numpy.append(temp)
        labels_for_numpy.append(temp2)

    data = np.array(data_for_numpy)
    use_shape = data.shape
    labels = np.array(labels_for_numpy)
    labels = (np.asarray(["{0}\n{1:.2f}".format(text, data) for text, data in \
        zip(labels.flatten(), data.flatten())])).reshape(use_shape)
    _, ax = plt.subplots(figsize=(10, 10))
    sb.heatmap(data, annot=labels, cmap="RdYlGn", fmt='', linewidths=.5, ax=ax)
    plt.savefig(os.path.join(DIRECTORY, file_name + ".png"), bbox_inches='tight')
