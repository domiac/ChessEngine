from board_mechanics import Board


class piece_moves(): # Should create 2 classes, one white one black. This will be white, renaming will happen later
    
    def __init__(self):
        pass

    def pawn_move1(self, Board, r, c):
        if Board[r-1][c]!=0: # If piece in front of pawn, can't move
            return False, Board
        else:
            Board[r-1,c]=Board[r,c]
            Board[r,c]=0
            return True, Board # Currently updates board directly, might need to create variable called pseudo_Board
        
    def pawn_move2(self, Board, r, c):
        if Board[r-1][c]!=0 or Board[r-2][c]!=0:
            return False, Board
        else:
            Board[r-2,c]=Board[r,c]
            Board[r,c]=0
            return True, Board # Same thing here as above.
        
    def pawn_take_left(self, Board, r, c):
        if Board[r-1,c-1] >= 0: # checks if the piece top left is a opponents piece
            return False, Board
        else:
            Board[r-1,c-1]=Board[r,c]
            Board[r,c]=0
            return True, Board

    def pawn_take_right(self, Board, r, c):
        if Board[r-1,c+1] >= 0: # checks if the piece top right is a opponents piece
            return False, Board
        else:
            print(True)
            Board[r-1,c+1]=Board[r,c]
            Board[r,c]=0
            return True, Board

