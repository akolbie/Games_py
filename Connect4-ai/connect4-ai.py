from board import Player()
from board import Board()

def get_best_move(board, player1, player2):
    if board.check_winner():
        print("Game complete - exiting")
        return
    
    for move in board.get_moves():
        best_score, best_move = -100, None
        temp_board = Board()
        temp_board.board = [row[:] for row in board.board]
        
