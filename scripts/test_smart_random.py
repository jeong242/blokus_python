import sys
import os
cwd = os.getcwd()
sys.path.insert(0, cwd+"/..")

import test_utils as T
from player_and_game import *

# DESCRIPTION of PLAYERS.
# weights[0] determines how important size of a piece is
# weights[1] determines how important maximizing the difference of my corners and opponent corners
# weights[2] decides how many of the best placements we choose to look ahead with
# weights[3] decides how important the score of the second move is
# weights[4] decides how important the score of the first move is

# <EDIT START
NUM_ITERATION = 20 
#SAVE_FILE_NAME = "min[1,1]_v_min[2,1]_%d.json" % NUM_ITERATION 
SAVE_FILE_NAME = "test_smart_random.json"
DEBUG = True 
# EDIT END/>

### RUN & SAVE ###
record_dicts = []

for i in range(NUM_ITERATION):
    print("################ Iteration %d ################" % (i+1) )

    # <EDIT START
    #first   = Greedy("A", "Minimax(1,1)A", Minimax_Player, [1, 1, 5, 1, 1])
    first  = Greedy("A", "SmartRandomA", Smart_Random_Player, [2, 1, 3, 5, 0])
    second  = Player("B", "RandomB", Random_Player)
    #third   = Greedy("C", "Minimax(2,1)C", Minimax_Player, [2, 1, 5, 1, 1])
    #third  = Greedy("C", "SmartRandomC", Smart_Random_Player)
    third  = Player("C", "RandomC", Random_Player)
    fourth  = Player("D", "RandomD", Random_Player)
    # EDIT END/>

    record_dicts += [T.run_test_all_general(first, second, third, fourth,DEBUG)]

T.save(record_dicts, SAVE_FILE_NAME)
