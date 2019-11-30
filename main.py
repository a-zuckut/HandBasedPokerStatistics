# main.py
''' Runner '''

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import log
logger = log.get_logger(__name__)
# get parameters

# right now we are only looking for 'ProfitPerHand' param
import argparse
from profit_per_hand import runner
from visualize import visualize

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-F", "--function", help="functions include: ProfitPerHand")
parser.add_argument("-D", "--directory", help="directory with data")
parser.add_argument("-v", "--visualize", help="Include to visualize (if supported)", action='store_true')
args = parser.parse_args()

data = None

if args.function == "ProfitPerHand":
	data = runner(args.directory, save=True)
else:
	logger.error("%s function is not implemented" % args.function)

if args.visualize:
	logger.info("Visualizing data for %s", args.function)
	visualize(args.function, data)

logger.debug("Executed")
