#!/usr/bin/env python
# <center>
# Michelle Cone | Theresa Gebert | Yuan Jiang
# </center>
# Blokus is a geometrically abstract, strategy board game that was invented in 2000. It can be a two- or four-player game. Each player has 21 pieces of a different color. The board is typically divided into 20 columns and 20 rows, but smaller two-player versions are 14x14.
# <center>
# <img src="http://2.bp.blogspot.com/_qmMWugrP-wo/TD0Ef45PsGI/AAAAAAAAH8g/f4ydzjee5rg/s1600/BlokusDuo.jpg">
# </center>
# <br>

# Here is a brief overview of the rules:
# 
#  1. A player can only place his/her own pieces diagonally touching to each other.
#  1. A player is allowed to touch pieces that are not his/her own orthogonally.
#  1. The goal is to end up with the smallest area in pieces left over once the board has been filled.
#  

# <headingcell level=3>

# Setting up the Game

# <markdowncell>

# The most important components of the game are the Game itself, the Players, the Board, and the pieces (Shapes). The Game coordinates actions between the Players and the Board. The Board has functions associated with it according to Shapes and Players. The implementations of these objects are provided below.

# <codecell>

# NECESSARY MODULES:

from utils import *
from player_and_game import *
from PIL import Image
from matplotlib import rcParams
rcParams['figure.figsize'] = (6, 6)
rcParams['figure.dpi'] = 150

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import copy
import pygame # Thanks to http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

# Parameters for BOARD:
BOARD_ROW = 20 
BOARD_COL = 20

# Parameters for GRAPICAL DISPLAY:
WIDTH = 20
HEIGHT = 20
MARGIN = 5
X = (WIDTH+MARGIN)*BOARD_COL + MARGIN
Y = (HEIGHT+MARGIN)*BOARD_ROW + MARGIN

print "\n \n Welcome to Blokus! \n \n \n Blokus is a geometrically abstract, strategy board game. It can be a two- or four-player game. Each player has 21 pieces of a different color. The two-player version of the board has 14 rows and 14 columns. \n \n You will be playing a two-player version against an algorithm of your choice: Random, Greedy, or Minimax. In case you need to review the rules of Blokus, please follow this link: http://en.wikipedia.org/wiki/Blokus. \n \n This is how choosing a move is going to work: after every turn, we will display the current state of the board, as well as the scores of each player and the pieces available to you. We have provided you with a map of the names of the pieces, as well as their reference points, denoted by red dots. When you would like to place a piece, we will prompt you for the name of the piece and the coordinate (column, row) of the reference point. If multiple placements are possible, we will let you choose which one you would like to play. \n \n Good luck! \n \n"

#img = Image.open('Images/Blokus_Tiles.png')
#img.show()

pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("PyBlokUs")
clock = pygame.time.Clock()

print "Please choose an algorithm to play against: \n A. Random \n B. Greedy \n C. Minimax \n"

choice = raw_input()

while not (choice in ["A", "B", "C"]):
    choice = raw_input("\n Please choose a valid algorithm: \n").upper()

if choice == "A":
    computer = Player("X", "Computer_A_R", Random_Player)
elif choice == "B":
    computer = Greedy("X", "Computer_A_G", Greedy_Player, [2, 1, 5, 1, 1])
else:
    computer = Greedy("X", "Computer_A_M", Minimax_Player, [3, 1, 8, 1, 1])

first = computer
#second = Greedy("B", "Computer_B", Minimax_Player, [2,1,30,1,1])
#second = Player("B", "Human_B", User_Player)
second = Player("B", "Computer_C", Random_Player)
third = Greedy("Y", "Computer_B", Greedy_Player, [2,1,30,1,1])
fourth = Player("D", "Computer_D", Random_Player)

#first = Player("A", "Computer_A", Random_Player)
#second = Player("B", "Computer_B", Random_Player)
#third = Player("C", "Computer_C", Random_Player)
#fourth = Player("D", "Computer_D", Random_Player)

standard_size = Board(BOARD_COL, BOARD_ROW, "_")

ordering = [first, second, third, fourth]
#random.shuffle(ordering)
userblokus = Blokus(ordering, standard_size, All_Shapes)

# <codecell>

userblokus.board.print_board(num = userblokus.rounds, fancy = False)
print "\n"
userblokus.play()
userblokus.board.print_board(num = userblokus.rounds, fancy = False)
print "\n"

while userblokus.winner() == "None":
    userblokus.play()
    userblokus.board.print_board(num = userblokus.rounds, fancy = False)
    print "\n"
    for p in userblokus.players:
        print p.name + " (" + str(p.score) + ") : " + str([s.ID for s in p.pieces])
        print 
    print "======================================================================="

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user pressed a key
            done = True  # Flag that we are done so we exit this loop
            print("CLOSING...")
            exit()

    # Set the screen background
    screen.fill(RED)
    for row in range(BOARD_ROW):
        print "here"
        for column in range(BOARD_COL):
            player = userblokus.board.state[row][column]
            # COLORS are defined in utils.py
            if player == 'X':
              color = RED
            elif player == 'B':
              color = YELLOW
            elif player == 'Y':
              color = BLUE
            elif player == 'D':
              color = GREEN
            else:
              color = WHITE
    
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(60)
    pygame.display.flip()

print 
userblokus.board.print_board()
print 
userblokus.play()

print "The final scores are..."

by_score = sorted(userblokus.players, key = lambda player: player.score)

for p in by_score:
    print p.name + " : " + str(p.score)
