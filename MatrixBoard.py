import numpy as np

from BoardFunctions import create_board, display_board


class MatrixBoard:
    def __init__(self, board_length, board_width, piece_locations, move_rules):
        self.move_rules = move_rules
        self.board_width = board_width
        self.board_length = board_length
        self.total_pieces = piece_locations
        self.board = create_board(board_length, board_width, piece_locations)


if __name__ == '__main__':
    BOARD_LENGTH = 8
    BOARD_WIDTH = 8
    PIECE_LOCATIONS = [
        (0, 0),
        (0, 2),
        (0, 4),
        (0, 6),

        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),

        (2, 0),
        (2, 2),
        (2, 4),
        (2, 6),
    ]

    MOVE_RULES = []

    board = MatrixBoard(BOARD_LENGTH, BOARD_WIDTH, PIECE_LOCATIONS, MOVE_RULES)

    print(display_board(board.board))
