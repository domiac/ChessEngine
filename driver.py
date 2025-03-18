# This file is the main app driver.

from board_mechanics import Board
from moves import piece_moves




def main():
    b = Board()
    board = b.board_init()
    p = piece_moves()
    print(p.pawn_take_right(board, 6, 0))






main()