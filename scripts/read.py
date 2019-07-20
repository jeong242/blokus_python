import sys
import os
cwd = os.getcwd()
sys.path.insert(0, cwd+"/..")
import test_utils as T

# not random any more.
all_random = "all_random.json"
greedy_v_greedy_20 = "greedy[2,1]_v_greedy[2,1]_20.json"

min_v_greedy_20 = "min[2,1]_v_greedy[2,1]_20.json"
greedy_v_min_20 = "greedy[2,1]_v_min[2,1]_20.json"

min_v_min_20_1 = "min[1,1]_v_min[2,1]_20.json"
min_v_min_20_2 = "min[2,1]_v_min[1,1]_20.json"

min_v_smartmin_20 = "min[2,1]_v_smartmin[2,1]_20.json"
smartmin_v_min_10 = "smartmin[2,1]_v_min[2,1]_10.json"

#FILENAME1 = min_v_greedy_20
FILENAME1 = min_v_smartmin_20 
#FILENAME2 = greedy_v_min_20

"""
loaded = T.load(FILENAME)
T.print_all(loaded)
print("\n")
"""
print(FILENAME1)
T.fprint_stat(FILENAME1)
#print(FILENAME2)
#T.fprint_stat(FILENAME2)
