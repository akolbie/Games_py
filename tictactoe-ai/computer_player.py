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
    
    return

def get_best_move(board, comp_sym, play_sym):
    best_score, best_move = -10, None
    temp_board = Board()
    for move in get_open_squares(board):
        temp_board.board = [row[:] for row in board.board]
        temp_board.add_move(*move, comp_sym)
        score = minimax(temp_board, False, comp_sym, play_sym, 1)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(board, maximizing, comp_sym, play_sym, depth):
    if board.check_winner() == (True, comp_sym): #computer wins
        return 1 / depth
    elif board.check_winner()[0]: #player wins
        return -1 / depth
    elif len(get_open_squares(board)) == 0: #draw
        return 0

    moves = get_open_squares(board)
    scores = []
    temp_board = Board()
    for move in moves:
        temp_board.board = [row[:] for row in board.board]
        if maximizing:
            player = comp_sym
        else:
            player = play_sym
        temp_board.add_move(*move, player)
        scores.append(minimax(temp_board, not maximizing, comp_sym, play_sym, depth + 1))
    if maximizing:
        return max(scores)
    return min(scores)