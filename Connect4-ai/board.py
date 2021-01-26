class Player():
    def __init__(self, player_symbol):
        self.symbol = player_symbol
        self.squares = []
        self.check_squares = []
        self.important_squares = [[2, 0], [2, 1], [2, 2], [2, 3], 
                                  [2, 4], [2, 5], [2, 6], [0, 3],
                                  [1, 3], [3, 3], [4, 3], [5, 3]]


    def add_move(self, move):
        self.squares.append(move)
        if move in self.important_squares:
            self.check_squares.append(move)
    
    def get_current_moves(self, board):
        self.squares = []
        self.check_squares = []
        for index_row, row in enumerate(board.board):
            for index_column, square in enumerate(row):
                if square == self.symbol:
                    self.add_move([index_row, index_column])

class Board():
    def __init__(self, player1, player2):
        self.rows = 6
        self.columns = 7
        self.players = [player1, player2]
        self.board = [[" " for i in range(self.columns)] for j in range(self.rows)]
        self.ordered_moves = []
        self.important_squares = [[2, 0], [2, 1], [2, 2], [2, 3], 
                                  [2, 4], [2, 5], [2, 6], [0, 3],
                                  [1, 3], [3, 3], [4, 3], [5, 3]]
    
    def __str__(self):
        to_return = ""
        for i in range(7):
            to_return = f"{to_return}  {i} |"
        line = "-" * 35
        to_return = f"{to_return}\n{line}\n"
        for i in self.board:
            to_return = f"{to_return}{i}\n"
        return to_return

    def add_move(self, column, player):
        try:
            self.column = int(column)
        except TypeError:
            print("Please enter an integer")
            return
        
        try:
            self.board[0][self.column]
        except IndexError:
            print("Selected Column does not exist")
            return
        
        for i in range(6):
            if self.board[self.rows - i - 1][self.column] == " ":
                self.board[self.rows - i - 1][self.column] = player.symbol
                player.add_move([self.rows - i - 1, self.column])
                self.ordered_moves.append([self.rows - i -1, self.column])
                return
        print("This column is already full")

    def del_last_move(self):
        last_move = self.ordered_moves.pop()
        self.board[last_move[0]][last_move[1]] = " "

    def get_moves(self):
        self.open_moves = []
        for i in range(self.columns):
            if self.board[0][i] == " ":
                self.open_moves.append(i)
        return self.open_moves

    def check_winner(self):
        directions = [[0, 1], [1, 0], [1, 1], [1, -1]]

        squares_in_row = 1
        for square in self.important_squares:
            if self.board[square[0]][square[1]] == " ":
                continue
            current_square = square
            square_value = self.board[square[0]][square[1]]
            for direction in directions:
                direct_multi = 1
                squares_in_row = 1
                current_square = square
                while True:
                    current_square = [current_square[0] + (direction[0] * direct_multi), 
                                      current_square[1] + (direction[1] * direct_multi)]
                    if current_square[0] < 0 or current_square[1] < 0:
                        break
                    try:
                        if self.board[current_square[0]][current_square[1]] == square_value:
                            squares_in_row += 1
                            if squares_in_row == 4:
                                return True, square_value
                        elif direct_multi == 1:
                            direct_multi = -1
                            current_square = square
                        else:
                            break
                    except IndexError:
                        if direct_multi == 1:
                            direct_multi = -1
                            current_square = square
                        else:
                            break
                        
        return False, " "
