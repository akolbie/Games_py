import board

p1 = board.Player("X")
p2 = board.Player("O")

a = board.Board(p1, p2)

a.board[0] = [" ", " ", "X", "X", "X", " ", " "]
a.check_winner()

print(a)
print(a.check_winner())