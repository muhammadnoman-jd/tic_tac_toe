def is_valid_move(position, board):
    return board[position - 1].isdigit()

def available_moves(board):
    for i, v in enumerate(board):
        if v.isdigit():
            yield i + 1
