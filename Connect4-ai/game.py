from board import Board
from board import Player
import ai_player

computer_player = Player("X")
human_player = Player("O")

current_board = Board(computer_player, human_player)
print(current_board)

while True:
    current_board.add_move(input("Select move"), human_player)
    print(current_board)
    if current_board.check_winner()[0]:
        print(f"Player {current_board.check_winner()[1]} is the winner")
        break
    if len(current_board.get_moves()) == 0:
        print("Game is a draw")
    current_board.add_move(ai_player.get_best_move(current_board, computer_player, human_player), computer_player)
    print(current_board)
    if current_board.check_winner()[0]:
        print(f"Player {current_board.check_winner()[1]} is the winner")
        break
    if len(current_board.get_moves()) == 0:
        print("Game is a draw")