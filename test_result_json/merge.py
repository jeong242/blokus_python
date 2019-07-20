import sys
import os
cwd = os.getcwd()
sys.path.insert(0, cwd+"/..")
import test_utils as T

# not random any more.
all_random = "all_random.json"
greedy_v_greedy_5 = "greedy[2,1]_v_greedy[2,1]_5.json"
greedy_v_greedy_15 = "greedy[2,1]_v_greedy[2,1]_15.json"
min_v_greedy_20 = "min[2,1]_v_greedy[2,1]_20.json"

FILENAME1 = greedy_v_greedy_5
FILENAME2 = greedy_v_greedy_15

loaded1 = T.load(FILENAME1)
loaded2 = T.load(FILENAME2)

T.save(loaded1+loaded2, "greedy[2,1]_v_greedy[2,1]_20.json")
