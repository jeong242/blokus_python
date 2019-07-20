#!/usr/bin/env python

save_json = "../test_result_json/"

# NECESSARY MODULES:

from utils import *
from player_and_game import *
from PIL import Image
from matplotlib import rcParams
rcParams['figure.figsize'] = (6, 6)
rcParams['figure.dpi'] = 150

import json
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import copy
import time
import stat_utils as S

# Parameters for BOARD:
BOARD_ROW = 20 
BOARD_COL = 20

#def run_test(first, second, third, fourth, DEBUG):

"""
choice = "A"
    
    if choice == "A":
        computer = Player("X", "Random_A_R", Random_Player)
elif choice == "B":
    computer = Greedy("X", "Greedy_A_G", Greedy_Player, [2, 1, 5, 1, 1])
    else:
        computer = Greedy("X", "Minimax_A_M", Minimax_Player, [3, 1, 8, 1, 1])

first = computer
    #second = Greedy("B", "Minimax_B", Minimax_Player, [2,1,30,1,1])
    second = Player("B", "Random_C", Random_Player)
    third = Greedy("Y", "Greedy_B", Greedy_Player, [2,1,30,1,1])
    fourth = Player("D", "Random_D", Random_Player)

second = Player("B", "Computer_C", Random_Player)
third = Greedy("Y", "Computer_B", Greedy_Player, [2,1,30,1,1])
fourth = Player("D", "Computer_D", Random_Player)
"""

"""
    GAME SETTING
        first   second
        fourth  thrid
"""
def run_test_all_general(first, second, third, fourth, DEBUG=False):
    ##### INIT #####
    # Init Blokus.
    standard_size = Board(BOARD_COL, BOARD_ROW, "_")
    ordering = [first, second, third, fourth]
    #random.shuffle(ordering)
    userblokus = Blokus(ordering, standard_size, All_Shapes)

    # record_dict store "total time", "avg time", "score", "winning place", "player info", "number of rounds" for each player.
    record_dict = {}
    # Init record_dict.r
    for p in userblokus.players:
        record = {}
        record["total_time"] = 0
        record_dict[p.name] = record
    
    record_dict["game"] = { "total_rounds":0 }
            
            
    ##### GAME PLAY #####
    # Note Do-while structure
    
    current_player = userblokus.players[0]
    # Measure time taken for current player.
    start = time.time()
    userblokus.play()
    end = time.time()
    # Store time taken for current player.
    record_dict[current_player.name]["total_time"] += end - start
    # Debug
    if DEBUG:
        print("Time taken to play = %d" % (end - start))
        userblokus.board.print_board(num = userblokus.rounds, fancy = False)
        print("\n")
        for p in userblokus.players:
            print(p.name + " (" + str(p.score) + ") : " + str([s.ID for s in p.pieces]))
        print("=======================================================================")

    while userblokus.winner() == "None":
        current_player = userblokus.players[0]
        # Measure time taken for current player.
        start = time.time()
        userblokus.play()
        end = time.time()
        # Store time taken for current player if it's not done.
        if not current_player.done:
            record_dict[current_player.name]["total_time"] += end - start
        # Debug
        if DEBUG:
            print("Time taken to play = %d" % (end - start))
      	    userblokus.board.print_board(num = userblokus.rounds, fancy = False)
            print("\n")
            for p in userblokus.players:
                if p.done:
                    print("Number of rounds "+str(p.rounds))
                print(p.name + " (" + str(p.score) + ") : " + str([s.ID for s in p.pieces]))
            print("=======================================================================")
    userblokus.play()

    ##### STORE DATA #####
    by_score = sorted(userblokus.players, key = lambda player: player.score)

    if DEBUG:
        print(userblokus.rounds)

    # record_dict store "total time", "avg time", "score", "winning place", "player info", "number of rounds" for each player.
    for i, p in enumerate(by_score):
        if not p.done:
            p.rounds = userblokus.rounds
            p.done = True
        record_dict[p.name]["number_of_rounds"] = p.rounds
        record_dict[p.name]["avg_time"] = record_dict[p.name]["total_time"] / p.rounds
        record_dict[p.name]["score"] = p.score
        record_dict[p.name]["winning_place"] = 4-i

    record_dict["game"]["total_rounds"] = userblokus.rounds
    
    return record_dict

# Run four random players.
def run_test_all_random(DEBUG=False):
    first = Player("A", "RandomA", Random_Player)
    second = Player("B", "RandomB", Random_Player)
    third = Player("C", "RandomC", Random_Player)
    fourth = Player("D", "RandomD", Random_Player)
    return run_test_all_general(first, second, third, fourth, DEBUG)

def run_two_random(first, third, DEBUG=False):
    second = Player("B", "RandomB", Random_Player)
    fourth = Player("D", "RandomD", Random_Player)
    return run_test_all_general(first, second, third, fourth, DEBUG)

# Save list of record_dict's.
def save(record_dicts, filename):
    with open(save_json+filename, 'w') as fp:
        json.dump(record_dicts, fp)

# Load list of record_dict's
def load(filename):
    with open(save_json+filename, 'r') as fp:
        return json.load(fp)

# Load then return stats (mean and sd)
def stat(filename):
    record_dicts = load(filename)
    names = [str(key) for key in record_dicts[0] if str(key) != "game"]

    attributes = [str(attr) for attr in record_dicts[0][names[0]]]
    
    # Build list of player p for some attribute.
    def build_list(p, attr):
        return [record_dict[p][attr] for record_dict in record_dicts]
    
    ### Init stat_dicts ###
    stat_dicts = {}
    for name in names:
        dict = {}
        for attr in attributes:
            dict[attr] = {"mean" : None, "sd"  : None}
        stat_dicts[name] = dict
    # Init for game
    dict = {}
    dict["total_rounds"] = {"mean" : None, "sd"  : None}
    dict["total_games"] = len(record_dicts)
    stat_dicts["game"] = dict

    ### Get stats ###
    for name in names:
        for attr in attributes:
            temp = build_list(name, attr)
            stat_dicts[name][attr]["mean"] = S.mean(temp)
            stat_dicts[name][attr]["sd"]   = S.sd(temp)
	# Get stats for first, second, third, fourth places.
    for name in names:
        temp = build_list(name, "winning_place")
        stat_dicts[name]["place"] = {}
        stat_dicts[name]["place"]["first"] = sum([1 for place in temp if place == 1]) 
        stat_dicts[name]["place"]["second"] = sum([1 for place in temp if place == 2]) 
        stat_dicts[name]["place"]["third"] = sum([1 for place in temp if place == 3]) 
        stat_dicts[name]["place"]["fourth"] = sum([1 for place in temp if place == 4]) 
		
    # Get stats for game
    temp = build_list("game", "total_rounds")
    stat_dicts["game"]["total_rounds"]["mean"] = S.mean(temp)
    stat_dicts["game"]["total_rounds"]["sd"]   = S.sd(temp)

    return stat_dicts

# Print out list of record_dict's
def print_all(record_dicts):
    names = [name for name in record_dicts[0]]
    name_lens = map(len, names)
    max_name_len = max(name_lens)
    format = "%-" + str(max_name_len) + "s"
    for record_dict in record_dicts:
        for key in record_dict:
            p_rec = record_dict[key]
            if key != "game":
                print((format+" : %d rounds / %.2f avg time / %d score / %d place")
                  % (key, p_rec["number_of_rounds"], p_rec["avg_time"],
                     p_rec["score"], p_rec["winning_place"]))
            else:
                print((format+" : %d total rounds") % (key, p_rec["total_rounds"]))
        print("")

def print_stat(stat):
    # Print stat for players.
    for player in stat:
        if player != "game":
            player_str = player + " :\n"
            for attr in stat[player]:
                if attr != "place":
                    player_str += ("\t%-17s --> mean = %8.3f / sd = %8.3f\n" % (attr, stat[player][attr]["mean"], stat[player][attr]["sd"]))
                else:
                    player_str += ("\t%-17s --> first = %d / second = %d / third = %d / fourth = %d\n" % (attr, stat[player][attr]["first"], stat[player][attr]["second"], stat[player][attr]["third"], stat[player][attr]["fourth"]))
            print(player_str)
    # Print stat for game.
    game_str = "game :\n"
    game_str += ("\t%-17s --> %d\n" % ("total_games", stat["game"]["total_games"]))
    game_str += ("\t%-17s --> mean = %8.3f / sd = %8.3f\n" % ("total_rounds", stat["game"]["total_rounds"]["mean"], stat["game"]["total_rounds"]["sd"]))
    print(game_str)

def fprint_stat(filename):
    stat_dict = stat(filename)
    print_stat(stat_dict)
