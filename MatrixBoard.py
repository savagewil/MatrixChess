import numpy as np

from BoardFunctions import create_board, display_board_matrix
from MoveFunctions import create_move_matrices, apply_moves


class MatrixBoard:
    def __init__(self, board_length, board_width, piece_locations, move_rules):
        self.move_rules = move_rules

        self.board_width = board_width
        self.board_length = board_length

        self.total_pieces = piece_locations

        self.board = create_board(board_length, board_width, piece_locations)

        self.move_pre, self.move_elimination, self.move_post = create_move_matrices(board_length, board_width, move_rules)


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


        (5, 1),
        (5, 3),
        (5, 5),
        (5, 7),

        (6, 0),
        (6, 2),
        (6, 4),
        (6, 6),

        (7, 1),
        (7, 3),
        (7, 5),
        (7, 7)
    ]

    MOVE_RULES = (['uf,df'] * 12) + (['ub,db'] * 12)


    board = MatrixBoard(BOARD_LENGTH, BOARD_WIDTH, PIECE_LOCATIONS, MOVE_RULES)

    print(display_board(board.board))

    # print("-------")
    # print(display_board(board.move_pre))
    #
    # print("-------")
    # print(display_board(board.move_elimination))
    #
    # print("-------")
    # print(display_board(board.move_post))

    print("================")
    # print(apply_moves(board.move_pre, board.move_elimination, board.move_post, board.board))

    # return np.dot(np.multiply(np.dot(pre_matrices, boards), elimination_matrix), post_matrices)
    new_shape = np.reshape(board.board, (BOARD_LENGTH, len(PIECE_LOCATIONS), BOARD_WIDTH))
    string = ""
    for a in new_shape:
        string += "\n"
        for b in a:
            string += " "
            for c in b:
                string += "%d" % (c)
    print(string)
