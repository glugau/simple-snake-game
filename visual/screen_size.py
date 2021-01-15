def make_screen_size(board_width, board_height, max_size):
    out = (0, 0)
    if board_width >= board_height:
        mult = float(max_size) / float(board_width)
    else:
        mult = float(max_size) / float(board_height)
    out = (int(board_width * mult) + 100, int(board_height * mult) + 100)
    return out
