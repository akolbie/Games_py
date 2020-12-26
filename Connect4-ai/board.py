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

    
    def check_win(self, board):
        directions = [[0, 1], [1, 0], [1, 1], [1, -1]]
        squares_in_row = 1
        for square in self.check_squares:
            current_square = square
            for direction in directions:
                direct_multi = 1 
                while True:
                    current_square = [current_square[0] + (direction[0] * direct_multi), 
                                      current_square[1] + (direction[1] * direct_multi)]
                    try:
                        if board.board[current_square[0]][current_square[1]] == self.symbol:
                            squares_in_row += 1
                            if squares_in_row == 4:
                                return True
                        elif direct_multi == 1:
                            direct_multi = -1 
                        else:
                            break
                    except IndexError:
                        if direct_multi == 1:
                            direct_multi = -1
                        else:
                            break
        return False
            

    

class Board():
    def __init__(self, player1, player2):
        self.rows = 6
        self.columns = 7
        self.players = [player1, player2]
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
        
        for i in range(7):
            print(self.rows - i - 1)
            if self.board[self.rows - i - 1][column] == " ":
                self.board[self.rows - i - 1][column] = player.symbol
                player.add_move([self.rows - i - 1, column])
                return
        print("This column is already full")

    def get_moves(self):
        self.open_moves = []
        for i in range(self.columns):
            if self.board[0][i] == " ":
                self.open_moves.append(i)
        return self.open_moves

    def check_winner(self):
        for player in self.players:
            if player.check_win(self):
                print(f"Player {player.symbol} wins")
