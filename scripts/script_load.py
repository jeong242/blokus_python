import sys
sys.path.insert(0, '/Users/minyoungjeong/Desktop/4511_project/Machine-Learning-Blokus-master')
import test_utils as T

loaded = T.load("all_random.json")
T.print_all(loaded)
print("\n")
T.fprint_stat("all_random.json")
