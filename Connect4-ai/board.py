class Board():
    def __init__(self):
        self.rows = 6
        self.columns = 7

        self.board = [[" " for i in range(self.columns)] for j in range(self.rows)]
    
    def __str__(self):
        to_return = ""
        for i in range(7):
            to_return = f"{to_return}  {i} |"
        line = "-" * 35
        to_return = f"{to_return}\n{line}\n"
        for i in self.board:
            to_return = f"{to_return}{i}\n"
        return to_return

    def add_move(self, column, symbol):
        try:
            self.column = int(column)
        except TypeError:
            print("Please enter an integer")   
        for i in range(7):
            if self.board[self.rows - i - 1][column] == " ":
                self.board[self.rows - i - 1][column] = symbol
                return
        print("This column is already full")

    def get_moves(self):
        self.open_moves = []
        for i in range(self.columns):
            if self.board[0][i] == " ":
                self.open_moves.append(i)
        return self.open_moves

    def check_winner(self):
        #only have to check a horizontal row (half way up the board) and the middle vertical row
        for index, square in enumerate(self.board[2]): #horizontal row
            

a = Board()

a.add_move(1,"X")
a.add_move(1,"X")
print(a)
print(a.get_moves())