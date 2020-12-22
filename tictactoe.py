from os import system

class Board():
    def __init__(self):
        self.board = [[" "," "," "] for i in range(3)]
    
    def add_move(self,row,column,player_symbol):
        try:
            self.row = int(row)
            self.column = int(column)
            self.player_symbol = player_symbol.upper()
        except ValueError:
            print("Please enter an integer for row and/or column")
            return
        if self.row > len(self.board) - 1 or self.column > len(self.board) - 1:
            print("Please enter an integer between 0 and 2")
            return
        if self.board[self.row][self.column] != " ":
            print("Move already selected, please pick an open space")
            return
        self.board[self.row][self.column] = self.player_symbol
        return

    def draw_board(self):
        horz_line = "-" * 16
        output = ["","",""]
        for index_row, row in enumerate(self.board):
            for index_square, square in enumerate(row):
                if index_square != 0:
                    output[index_row] += "|"
                output[index_row] += f"  {square}  "
        output.append(horz_line)
        output = [output[0],output[3],output[1],output[3],output[2]]
        system("cls")
        for row in output:
            print(row)
        
    def check_winner(self):
        for index_row in range(3):
            place_holder = self.board[index_row][0]
            if place_holder == " ":
                continue
            for index_column in range(3):
                if self.board[index_row][index_column] != place_holder:
                    break
                if index_column == 2:
                    return True, place_holder

        for index_column in range(3):
            place_holder = self.board[0][index_column]
            if place_holder == " ":
                continue
            for index_row in range(3):
                if self.board[index_row][index_column] != place_holder:
                    break
                if index_row == 2:
                    return True, place_holder
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            print(f"{self.board[0][0]} is the winner")
            return True, self.board[1][1]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            print(f"{self.board[1][1]} is the winner")
            return True, self.board[1][1]
        
        return False, " "

