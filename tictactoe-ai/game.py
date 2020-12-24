import tictactoe as ttt
import computer_player as cp

current_board = ttt.Board()

def get_player_move(play_sym):
    while True:
        try:
            row = int(input("Enter row"))
            column = int(input("Enter column"))
        except ValueError:
            print("Please input integers")
        if row < 3 or column < 3:
            return row, column, play_sym
        print("Entered value must be between 0-2")

PLAYER_SYMBOL = "X"
COMPUTER_SYMBOL = "O"

while True:
    current_board.draw_board()
    current_board.add_move(*get_player_move(PLAYER_SYMBOL))
    current_board.draw_board()
    if current_board.check_winner()[0]:
        print("Player wins")
        break
    if len(cp.get_open_squares(current_board)) == 0:
        print("Tie")
        break
    current_board.add_move(*cp.get_best_move(current_board,COMPUTER_SYMBOL,PLAYER_SYMBOL),COMPUTER_SYMBOL)
    current_board.draw_board()
    if current_board.check_winner()[0]:
        print("Computer wins")
        break
    if len(cp.get_open_squares(current_board)) == 0:
        print("Tie")
        break
    
    