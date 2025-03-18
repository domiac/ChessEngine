# This file is the main app driver.
import chess
from move_generator import Analyzer


def main():
    board = chess.Board()
    analyzer = Analyzer(depth=2)  # Create an instance of Analyzer with a depth of 3
    analyzer.move_analyzer(board)






main()