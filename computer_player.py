from tictactoe import Board

def get_open_squares(board):
    list_open_squares = []
    for row_index, row in enumerate(board.board):
        for column_index, square in enumerate(row):
            if square == " ":
                list_open_squares.append([row_index, column_index])
    return list_open_squares

def check_win(board, moves, comp_sym):
    temp_board = Board()
    for move in moves:
        temp_board.board = [row[:] for row in board.board]
        temp_board.add_move(*move, comp_sym)
        if temp_board.check_winner()[0]:
            return move

def check_lose(board, moves, play_sym):
    temp_board = Board()
    for move in moves:
        temp_board.board = [row[:] for row in board.board]
        temp_board.add_move(*move, play_sym)
        if temp_board.check_winner()[0]:
            return move

def make_dict(moves):
    return {move:0 for move in moves}


def select_move(current_board, comp_symbol, play_symbol):
    #import current game board and computer's symbol

    #make a list of open squares
    list_open_squares = get_open_squares(current_board)
    #if all squares open, make move to top left corner
    if len(list_open_squares) == 9:
        return 0,0,comp_symbol

    if check_win(current_board, list_open_squares, comp_symbol):
        return *check_win(current_board, list_open_squares, comp_symbol), comp_symbol
    
    if check_lose(current_board, list_open_squares, play_symbol):
        return *check_lose(current_board, list_open_squares, play_symbol), comp_symbol
    
    move_ratings = make_dict(list_open_squares)
    
    for move in list_open_squares:

    # add open squares to a dict eg [1,2]:0
    #   dict is used to track move "value"
    return