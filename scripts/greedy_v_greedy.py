import sys
sys.path.insert(0, '/Users/minyoungjeong/Desktop/4511_project/Machine-Learning-Blokus-master')
import test_utils as T
from player_and_game import *

# DESCRIPTION of PLAYERS.
# weights[0] determines how important size of a piece is
# weights[1] determines how important maximizing the difference of my corners and opponent corners
# weights[2] decides how many of the best placements we choose to look ahead with
# weights[3] decides how important the score of the second move is
# weights[4] decides how important the score of the first move is

# <EDIT START
NUM_ITERATION = 15
SAVE_FILE_NAME = "min_v_min_%d.json" % NUM_ITERATION
# EDIT END/>

### RUN & SAVE ###
record_dicts = []

for i in range(NUM_ITERATION):
    print("################ Iteration %d ################" % (i+1) )

    # <EDIT START
    first   = Greedy("A", "Greedy(2,1)A", Greedy_Player, [2, 1, 5, 1, 1])
    second  = Player("B", "RandomB", Random_Player)
    third   = Greedy("C", "Greedy(2,1)C", Greedy_Player, [2, 1, 5, 1, 1])
    fourth  = Player("D", "RandomD", Random_Player)
    # EDIT END/>

    record_dicts += [T.run_test_all_general(first, second, third, fourth,True)]

T.save(record_dicts, SAVE_FILE_NAME)
