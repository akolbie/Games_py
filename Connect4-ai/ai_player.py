from board import Player
from board import Board

def get_best_move(board, comp_player, human_player):
    if board.check_winner()[0]:
        print("Game complete - exiting")
        return
    best_score, best_move = -100, None
    temp_board = Board(comp_player, human_player)
    temp_board.board = [row[:] for row in board.board]
    
    for move in temp_board.get_moves():
        temp_board.add_move(move, comp_player)
        score = minimax(temp_board, False, comp_player, human_player, 1)
        temp_board.del_last_move()
        if score > best_score:
            best_score = score
            best_move = move
    if best_move == None:
        return 3
    return best_move


def minimax(board, maximizing, comp_player, human_player, depth):
    if depth == 7:
        return 0
    if board.check_winner() == (True, comp_player.symbol):
        return 10 / depth
    elif board.check_winner()[0]:
        return -10 / depth
    elif len(board.get_moves()) == 0:
        return 0
    
    moves = board.get_moves()
    scores = []

    for move in moves:
        if maximizing:
            board.add_move(move, comp_player)
            scores.append(minimax(board, not maximizing, comp_player, human_player, depth + 1))
            board.del_last_move()
        else:
            board.add_move(move, human_player)
            scores.append(minimax(board, not maximizing, comp_player, human_player, depth + 1))
            board.del_last_move()
    if maximizing:
        return max(scores)
    return min(scores)
