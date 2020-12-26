import board

p1 = board.Player("X")
p2 = board.Player("O")

a = board.Board(p1, p2)

a.board[0] = ["X", "X", "X", "X", " ", " ", " "]
p1.get_current_moves(a)

print(a)
print(p1.check_win(a))