# This file will contain the chess board mechanics
import numpy as np





class Board():
    def __init__(self):
        self.p = {
            'P': 1,     # Pawn
            'N': 3,     # Knight
            'B': 3,     # Bishop
            'R': 5,     # Rook
            'Q': 9,     # Queen
            'K': np.inf # King probably need to change to undefined
        }


    def board_init(self):
        baseBoard = np.array([[-self.p['R'], -self.p['N'], -self.p['B'], -self.p['Q'], -self.p['K'], -self.p['B'], -self.p['N'], -self.p['R']],
                            [-self.p['P'], -self.p['P'], -self.p['P'], -self.p['P'], -self.p['P'], -self.p['P'], -self.p['P'], -self.p['P']],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,-self.p['R'],0,0,0,0,0,0],
                            [self.p['P'], self.p['P'], self.p['P'], self.p['P'], self.p['P'], self.p['P'], self.p['P'], self.p['P']],
                            [self.p['R'], self.p['N'], self.p['B'], self.p['Q'], self.p['K'], self.p['B'], self.p['N'], self.p['R']]])
        return baseBoard

    def update_board(self):
        pass

    def move(self, piece):
        pass

