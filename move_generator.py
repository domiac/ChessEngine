import chess



class Analyzer:
    def __init__(self, depth):
        self.depth = depth

    
    def move_analyzer(self, board, current_depth=0):
        all_legal_moves = board.legal_moves
        copy_of_board = board.copy()
        
        for move in all_legal_moves:
            if copy_of_board.is_valid():
                copy_of_board.push(move)
                print(copy_of_board)
                if current_depth + 1 < self.depth:
                    # Recursively call move_analyzer with incremented depth
                    self.move_analyzer(copy_of_board, current_depth + 1)
                else:
                    # Reached the desired depth, perform analysis or other actions
                    break


            
    

        

            

    
