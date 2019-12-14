import numpy as np
import MoveFunctions
import BoardFunctions
import TranslationMatrices
import MatrixBoard


BOARD_LENGTH = 8
BOARD_WIDTH = 8
PIECE_LOCATIONS = [
    # (0, 0),
    # (0, 2),
    # (0, 4),
    # (0, 6),

    # (1, 1),
    (1, 3),
    # (1, 5),
    # (1, 7),

    # (2, 0),
    # (2, 2),
    # (2, 4),
    # (2, 6),


    # (5, 1),
    # (5, 3),
    # (5, 5),
    # (5, 7),

    # (6, 0),
    # (6, 2),
    (6, 4),
    # (6, 6),

    # (7, 1),
    # (7, 3),
    # (7, 5),
    # (7, 7)
]

MOVE_RULES = (['uf,df'] * 1) + (['ub,db'] * 1)


board = BoardFunctions.create_board(BOARD_LENGTH, BOARD_WIDTH, PIECE_LOCATIONS)
pre_matrices, elimination_matrix, post_matrices, move_count_array = MoveFunctions.create_move_matrices(BOARD_LENGTH, BOARD_WIDTH, MOVE_RULES)
transform = MoveFunctions.create_piece_to_move_matrix(BOARD_LENGTH, BOARD_WIDTH, move_count_array)

print(BoardFunctions.display_board_matrix(board))
print("==============transform===============")
print(BoardFunctions.display_board_matrix(transform))
print(board.shape)
print(transform.shape)

print("==============moves_space===============")
moves_space = board.dot(transform)
print(BoardFunctions.display_board_matrix(moves_space))
print(moves_space.shape)


print("==============pre_matrices===============")
print(BoardFunctions.display_board_matrix(pre_matrices))
print(pre_matrices.shape)

print("=============elimination_matrix================")
print(BoardFunctions.display_board_matrix(elimination_matrix))
print(elimination_matrix.shape)

print("=============post_matrices================")
print(BoardFunctions.display_board_matrix(post_matrices))
print(post_matrices.shape)

print("============ shift 1 =================")
shift1 = pre_matrices.dot(moves_space)
print(BoardFunctions.display_board_matrix(shift1))
print(shift1.shape)

print("============ elim =================")
elim = np.multiply(elimination_matrix, shift1)
print(BoardFunctions.display_board_matrix(elim))
print(elim.shape)

print("============ shift 2 =================")
shift2 = elim.dot(post_matrices)
print(BoardFunctions.display_board_matrix(shift2))
print(shift2.shape)
