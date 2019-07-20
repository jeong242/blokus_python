# Run four random players.
NUM_ITERATION = 2

import sys
sys.path.insert(0, '/Users/minyoungjeong/Desktop/4511_project/Machine-Learning-Blokus-master')

import test_utils as T

record_dicts = []

for i in range(NUM_ITERATION):
	record_dicts += [T.run_test_all_random()]

T.save(record_dicts, "all_random.json")
