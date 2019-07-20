import sys\nsys.path.insert(0, '/Users/minyoungjeong/Desktop/4511_project/Machine-Learning-Blokus-master')
import test_utils as T

result = T.run_test_all_random(True)
T.save([result], "test.json")
