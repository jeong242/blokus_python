"""
    Contains SHAPES and BOARD.
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import copy

from PIL import Image                                                                                
from matplotlib import rcParams
rcParams['figure.figsize'] = (6, 6)
rcParams['figure.dpi'] = 150

# Define some colors for DISPLAY
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# <headingcell level=4>

# SHAPES

# <codecell>

# Here we define necessary functions for rotating a point about another point.
# They are used in the definition of the Shape class.

def rotatex((x, y), (refx, refy), deg):
    """
    Returns the new x value of a point (x, y)
    rotated about the point (refx, refy) by
    deg degrees clockwise.
    """
    return (math.cos(math.radians(deg))*(x - refx)) + (math.sin(math.radians(deg))*(y - refy)) + refx

def rotatey((x, y), (refx, refy), deg):
    """
    Returns the new y value of a point (x, y)
    rotated about the point (refx, refy) by
    deg degrees clockwise.
    """
    return (- math.sin(math.radians(deg))*(x - refx)) + (math.cos(math.radians(deg))*(y - refy)) + refy

def rotatep(p, ref, d):
    """
    Returns the new point as an integer tuple
    of a point p (tuple) rotated about the point
    ref (tuple) by d degrees clockwise.
    """
    return (int(round(rotatex(p, ref, d))), int(round(rotatey(p, ref, d))))

# <codecell>

# Here we implement the Shape class. Using math and geometrical formulae,
# we were able to implement rotate and flip functions that work for all 21 shapes
# and greatly reduced the length of our code.
#
# A subclass that inherits from Shape is expected to override methods like
# "ID", "size", and "points" to reflect the characteristics of that particular
# shape.

class Shape(object):
    """
    A class that defines the functions associated
    with a shape.
    """
    def __init__(self):
        self.ID = "None" 
        self.size = 1
    
    def create(self, num, pt):
        self.set_points(0, 0)
        pm = self.points
        self.points_map = pm
        
        self.refpt = pt
        x = pt[0] - self.points_map[num][0]
        y = pt[1] - self.points_map[num][1]
        self.set_points(x, y)
    
    def set_points(self, x, y):
        self.points = []
        self.corners = []
        
    def rotate(self, degrees):
        """
        Returns the points that would be covered by a
        shape that is rotated 0, 90, 180, of 270 degrees
        in a clockwise direction.
        """
        assert(self.points != "None")
        assert(degrees in [0, 90, 180, 270])
        
        def rotate_this(p):
            return(rotatep(p, self.refpt, degrees))
        
        self.points = map(rotate_this, self.points)
        self.corners = map(rotate_this, self.corners)
        
    def flip(self, orientation):
        """
        Returns the points that would be covered if the shape
        was flipped horizontally or vertically.
        """
        assert(orientation == "h" or orientation == "None")
        assert(self.points != "None")
        
        def flip_h(p):
            x1 = self.refpt[0]
            x2 = p[0]
            x1 = (x1 - (x2 - x1))
            return (x1, p[1])
        
        def no_flip(p):
            return p
        
        # flip the piece horizontally
        if orientation == "h":
            self.points = map(flip_h, self.points)
            self.corners = map(flip_h, self.corners)
        # flip the piece vertically
        elif orientation == "None":
            self.points = map(no_flip, self.points)
            self.corners = map(no_flip, self.corners)
        else: raise Exception("Invalid orientation.")

# <markdowncell>

# The following is a map of all of the shapes in the game of Blokus. It is not difficult to add shapes to this game as long as the user specifies the size, points, and corners associated with that shape.

# Implement all of the shapes according to the Shape
# class defined earlier and according to the image above.
# The highlighted point is the generation point and the
# numbers represent the order in which points will be
# listed in the points variable.
#
# The ID will always be set to the name next to each shape.

# Implement all of the shapes according to the Shape
# class defined earlier and according to the image above.
# The highlighted point is the generation point and the
# numbers represent the order in which points will be
# listed in the points variable.
#
# The ID will always be set to the name next to each shape.

class I1(Shape):
    def __init__(self):
        self.ID = "I1"
        self.size = 1
    def set_points(self, x, y):
        self.points = [(x, y)]
        self.corners = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]

class I2(Shape):
    def __init__(self):
        self.ID = "I2"
        self.size = 2
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1)]
        self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 2), (x - 1, y + 2)]

class I3(Shape):
    def __init__(self):
        self.ID = "I3"
        self.size = 3
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2)]
        self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 3), (x - 1, y + 3)]

class I4(Shape):
    def __init__(self):
        self.ID = "I4"
        self.size = 4
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)]
        self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 4), (x - 1, y + 4)]

class I5(Shape):
    def __init__(self):
        self.ID = "I5"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3), (x, y + 4)]
        self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 5), (x - 1, y + 5)]

class V3(Shape):
    def __init__(self):
        self.ID = "V3"
        self.size = 3
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y)]
        self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2)]

class L4(Shape):
    def __init__(self):
        self.ID = "L4"
        self.size = 4
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2), (x + 1, y)]
        self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 3), (x - 1, y + 3)]

class Z4(Shape):
    def __init__(self):
        self.ID = "Z4"
        self.size = 4
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x - 1, y)]
        self.corners = [(x - 2, y - 1), (x + 1, y - 1), (x + 2, y), (x + 2, y + 2), (x - 1, y + 2), (x - 2, y + 1)]

class O4(Shape):
    def __init__(self):
        self.ID = "O4"
        self.size = 4
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y)]
        self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 2), (x - 1, y + 2)]

class L5(Shape):
    def __init__(self):
        self.ID = "L5"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x + 3, y)]
        self.corners = [(x - 1, y - 1), (x + 4, y - 1), (x + 4, y + 1), (x + 1, y + 2), (x - 1, y + 2)]

class T5(Shape):
    def __init__(self):
        self.ID = "T5"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2), (x - 1, y), (x + 1, y)]
        self.corners = [(x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 3), (x - 1, y + 3), (x - 2, y + 1), (x - 2, y - 1)]

class V5(Shape):
    def __init__(self):
        self.ID = "V5"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x, y + 2), (x + 1, y), (x + 2, y)]
        self.corners = [(x - 1, y - 1), (x + 3, y - 1), (x + 3, y + 1), (x + 1, y + 3), (x - 1, y + 3)]

class N(Shape):
    def __init__(self):
        self.ID = "N"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x + 1, y), (x + 2, y), (x, y - 1), (x - 1, y - 1)]
        self.corners = [(x + 1, y - 2), (x + 3, y - 1), (x + 3, y + 1), (x - 1, y + 1), (x - 2, y), (x - 2, y - 2)]

class Z5(Shape):
    def __init__(self):
        self.ID = "Z5"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y - 1)]
        self.corners = [(x + 2, y - 1), (x + 2, y + 2), (x, y + 2), (x - 2, y + 1), (x - 2, y - 2), (x, y - 2)]

class T4(Shape):
    def __init__(self):
        self.ID = "T4"
        self.size = 4
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y), (x - 1, y)]
        self.corners = [(x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1)]

class P(Shape):
    def __init__(self):
        self.ID = "P"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x, y - 2)]
        self.corners = [(x + 1, y - 3), (x + 2, y - 2), (x + 2, y + 1), (x - 1, y + 1), (x - 1, y - 3)]

class W(Shape):
    def __init__(self):
        self.ID = "W"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x - 1, y - 1)]
        self.corners = [(x + 1, y - 1), (x + 2, y), (x + 2, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 2), (x, y - 2)]

class U(Shape):
    def __init__(self):
        self.ID = "U"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x, y - 1), (x + 1, y - 1)]
        self.corners = [(x + 2, y - 2), (x + 2, y), (x + 2, y + 2), (x - 1, y + 2), (x - 1, y - 2)]

class F(Shape):
    def __init__(self):
        self.ID = "F"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x, y - 1), (x - 1, y)]
        self.corners = [(x + 1, y - 2), (x + 2, y), (x + 2, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2)]

class X(Shape):
    def __init__(self):
        self.ID = "X"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        self.corners = [(x + 1, y - 2), (x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2)]

class Y(Shape):
    def __init__(self):
        self.ID = "Y"
        self.size = 5
    def set_points(self, x, y):
        self.points = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x - 1, y)]
        self.corners = [(x + 3, y - 1), (x + 3, y + 1), (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1)]

# <headingcell level=4>

# BOARD

# <codecell>

# Playing Blokus requires an interface.
# Our interface is a square board, which we will
# represent as a list of lists.
#
#      e.g. [[1,2],[3,4]] is the following board:
#
#           | 1 2 |
#           | 3 4 |
#
# Write a function that lets us print such a board.

def printBoard(board):
    n = 2
    """
        Prints the board where the representation of a board is
        a list of row-lists. The function throws an error if the
        the board is invalid: the length of the rows are not
        the same.
        """
    assert(len(set([len(board[i]) for i in xrange(len(board))])) == 1)
    print ' ' * n,
    for i in range(len(board[1])):
        print str(i) + ' ' * (n-len(str(i))),
    print
    for i, row in enumerate(board):
        print str(i) + ' ' * (n-len(str(i))), (' ' * n).join(row)

# Credit to Sukrit Kalra for inspiration.
# http://stackoverflow.com/questions/16541973/print-matrix-with-indicies-python

# <codecell>

# This function uses MatplotLib to create a fancy image
# of the board that opens in a separate window.

def fancyBoard(board, num):
    
    Apoints = []
    Bpoints = []
    
    for y in enumerate(board.state):
        for x in enumerate(y[1]):
            if x[1] == "A":
                Apoints.append((x[0], (board.size[0] - 1) - y[0]))
            if x[1] == "B":
                Bpoints.append((x[0], (board.size[0] - 1) - y[0]))
    
    # fig = plt.figure(frameon=False)
    ax = plt.subplot(111, xlim=(0, board.size[0]), ylim=(0, board.size[1]))
    
    for i in xrange(board.size[0] + 1):
        for j in xrange(board.size[1] + 1):
            polygon = plt.Polygon([[i, j], [i + 1, j], [i + 1, j + 1], [i, j + 1], [i, j]])
            if (i, j) in Apoints:
                polygon.set_facecolor('red')
                ax.add_patch(polygon)
            elif (i, j) in Bpoints:
                polygon.set_facecolor('blue')
                ax.add_patch(polygon)
            else:
                polygon.set_facecolor('lightgrey')
                ax.add_patch(polygon)
    
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_formatter(plt.NullFormatter())
        axis.set_major_locator(plt.NullLocator())
    
    plt.savefig("random" + str(num) + ".png")
#plt.show()
# return ax

# Credit to Jake Vanderplas <vanderplas@astro.washington.edu>,  Dec. 2012
# for inspiration for this code.
# http://jakevdp.github.io/blog/2012/12/06/minesweeper-in-matplotlib/

# Here we implement the Board class. Boards take in
# Players and update according to placements made.
# They also have a print functionality.

class Board:
    """
        Creates a board that has n rows and
        m columns with an empty space represented
        by a character string according to null of
        character length one.
        """
    def __init__(self, n, m, null):
        self.size = (n, m)
        self.null = null
        self.empty = [[self.null] * m for i in xrange(n)]
        self.state = self.empty
    
    def update(self, player, move):
        """
            Takes in a Player object and a move as a
            list of integer tuples that represent the piece.
            """
        for row in xrange(len(self.state)):
            for col in xrange(len(self.state[1])):
                if (col, row) in move:
                    self.state[row][col] = player.label
    
    def in_bounds(self, point):
        """
            Takes in a tuple and checks if it is in the bounds of
            the board.
            """
        return (0 <= point[0] <= (self.size[1] - 1)) & (0 <= point[1] <= (self.size[0] - 1))
    
    def overlap(self, move):
        """
            Returns a boolean for whether a move is overlapping
            any pieces that have already been placed on the board.
            """
        if False in [(self.state[j][i] == self.null) for (i, j) in move]:
            return(True)
        else: return(False)
    
    def corner(self, player, move):
        """
            Note: ONLY once a move has been checked for adjacency, this
            function returns a boolean; whether the move is cornering
            any pieces of the player proposing the move.
            """
        validates = []
        
        for (i, j) in move:
            if self.in_bounds((j + 1, i + 1)):
                validates.append((self.state[j + 1][i + 1] == player.label))
            
            if self.in_bounds((j - 1, i - 1)):
                validates.append((self.state[j - 1][i - 1] == player.label))
            
            if self.in_bounds((j - 1, i + 1)):
                validates.append((self.state[j - 1][i + 1] == player.label))
            
            if self.in_bounds((j + 1, i - 1)):
                validates.append((self.state[j + 1][i - 1] == player.label))
        
        if True in validates: return True
        else: return False
    
    def adj(self, player, move):
        """
            Checks if a move is adjacent to any squares on
            the board which are occupied by the player
            proposing the move and returns a boolean.
            """
        validates = []
        
        for (i, j) in move:
            if self.in_bounds((j, i + 1)):
                validates.append((self.state[j][i + 1] == player.label))
            
            if self.in_bounds((j, i - 1)):
                validates.append((self.state[j][i - 1] == player.label))
            
            if self.in_bounds((j - 1, i)):
                validates.append((self.state[j - 1][i] == player.label))
            
            if self.in_bounds((j + 1, i)):
                validates.append((self.state[j + 1][i] == player.label))
        
        if True in validates: return True
        else: return False
    
    def print_board(self, num = None, fancy = False):
        if fancy == False:
            printBoard(self.state)
        else: fancyBoard(self, num)

# <headingcell level=4>

# PLAYERS

# <codecell>

# Here we implement the Player class. Players interact
# with Boards and Games. They can propose moves,
# which can be rejected if the move is invalid.
# They play according to a certain strategy,  as
# specified by a function that takes in the current
# state of the game's interface and returns a placement.

class Player:
    def __init__(self, label, name, strategy):
        self.label = label
        self.name = name
        self.pieces = []
        self.corners = set()
        self.strategy = strategy
        self.score = 0
    
    def add_pieces(self, pieces):
        """
            Gives a player the initial set of pieces.
            """
        self.pieces = pieces
    
    def start_corner(self, p):
        """
            Gives a player an initial starting corner.
            """
        self.corners = set([p])
    
    def remove_piece(self, piece):
        """
            Removes a given piece (Shape object) from
            the list of pieces a player has.
            """
        self.pieces = [s for s in self.pieces if s.ID != piece.ID]
    
    def update_player(self, placement, board):
        """
            Updates the variables that the player is keeping track
            of, e.g. their score and their available corners.
            Placement should be in the form of a Shape object.
            """
        self.score = self.score + placement.size
        for c in placement.corners:
            if (board.in_bounds(c) and (not board.overlap([c]))):
                (self.corners).add(c)
    
    def possible_moves(self, pieces, game):
        """
            Returns a unique list of placements, i.e. Shape objects
            with a particular flip, orientation, corners, and points.
            It uses a list of pieces (Shape objects) and the game, which includes
            its rules and valid moves, in order to find the placements.
            """
        def check_corners(game):
            """
                Updates the corners of the player, in case the
                corners have been covered by another player's pieces.
                """
            self.corners = set([(i,j) for (i,j) in self.corners if game.board.state[j][i] == game.board.null])
        
        # Check the corners before proceeding.
        check_corners(game)
        
        # This list of placements will be updated with valid ones.
        placements = []
        visited = []
        
        # Loop through every available corner.
        for cr in self.corners:
            # Look through every piece offered. (This will be restricted according
            # to certain algorithms.)
            for sh in pieces:
                # Create a new shape so that the one in the player's
                # list of shapes is not overwritten.
                try_out = copy.deepcopy(sh)
                # Loop over every potential refpt the piece could have.
                for num in xrange(try_out.size):
                    try_out.create(num, cr)
                    # And every possible flip.
                    for fl in ["h", "None"]:
                        try_out.flip(fl)
                        # And every possible orientation.
                        for rot in [90]*4:
                            try_out.rotate(rot)
                            candidate = copy.deepcopy(try_out)
                            if game.valid_move(self, candidate.points):
                                if not (set(candidate.points) in visited):
                                    placements.append(candidate)
                                    visited.append(set(candidate.points))
        
        return placements
    
    def do_move(self, game):
        """
            Generates a move according to the Player's
            strategy and current state of the board.
            """
        return self.strategy(self, game)
