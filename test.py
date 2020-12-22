import tictactoe as ttt
import computer_player as cp

a = ttt.create_board()
print(a.board)
print(cp.get_best_move(a,"O","X"))