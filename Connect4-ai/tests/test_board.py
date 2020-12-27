
from board import Board
from board import Player

def test_check_win_a():
    p1 = Player("X")
    p2 = Player("O")
    board = Board(p1, p2)

    board.add_move(3, p2)
    board.add_move(3, p1)
    board.add_move(2, p2)
    board.add_move(4, p1)
    assert board.check_winner()[0] == False