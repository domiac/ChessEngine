# This file will contain the chess board mechanics
import numpy as np




p = {
    'P': 1,     # Pawn
    'N': 3,     # Knight
    'B': 3,     # Bishop
    'R': 5,     # Rook
    'Q': 9,     # Queen
    'K': np.inf # King
}



def board():
    baseBoard = np.array([[-p['R'],-p['N'], -p['B'], -p['Q'],-p['K'],-p['B'],-p['N'], -p['R']],
                          [-p['P'],-p['P'], -p['P'], -p['P'],-p['P'],-p['P'],-p['P'], -p['P']],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [p['P'],p['P'], p['P'], p['P'],p['P'],p['P'],p['P'], p['P']],
                         [p['R'],p['N'], p['B'], p['Q'],p['K'],p['B'],p['N'], p['R']]])
    return baseBoard



