import numpy as np
import TranslationMatrices
from BoardFunctions import display_board_matrix

NUMBERS = "1234567890"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def create_move_matrices(board_length, board_width, move_array):
    pre_matrices = None
    post_matrices = None
    move_count_array = []
    for moves in move_array:
        split_moves = moves.split(",")
        move_count_array.append(len(split_moves))
        for move in split_moves:
            pre_matrix, post_matrix = create_one_move(move)
            if pre_matrices is None:
                pre_matrices = pre_matrix
            else:
                pre_matrices = np.concatenate((pre_matrices, pre_matrix), 0)

            if post_matrices is None:
                post_matrices = post_matrix
            else:
                post_matrices = np.concatenate((post_matrices, post_matrix), 0)
    elimination_matrix = create_elimination_matrix2(board_length, board_width, move_count_array)
    return pre_matrices, elimination_matrix, post_matrices, move_count_array


def create_piece_to_move_matrix(board_length, board_width, move_count_array):
    length = board_length * len(move_count_array)
    width = board_width * sum(move_count_array)
    elimination_matrix = np.zeros((length, width))
    y_displacement = 0
    for piece_index in range(len(move_count_array)):
        for move_index in range(move_count_array[piece_index]):
            elimination_matrix[piece_index * board_width:(piece_index + 1) * board_width,
            y_displacement * board_length:(y_displacement + 1) * board_length] += np.eye(board_width)
            y_displacement += 1
    return elimination_matrix


def create_elimination_matrix(board_length, board_width, move_count_array):
    length = board_length * sum(move_count_array)
    width = board_width * len(move_count_array)
    elimination_matrix = np.zeros((length, width))
    y_displacement = 0
    for piece_index in range(len(move_count_array)):
        for move_index in range(move_count_array[piece_index]):
            elimination_matrix[y_displacement * board_width:(y_displacement + 1) * board_width,
            piece_index * board_length:(piece_index + 1) * board_length] += 1
            y_displacement += 1
    return elimination_matrix


def create_elimination_matrix2(board_length, board_width, move_count_array):
    length = board_length * sum(move_count_array)
    width = board_width * sum(move_count_array)
    elimination_matrix = np.zeros((length, width))

    for i in range(sum(move_count_array)):
        elimination_matrix[i * board_width:(i + 1) * board_width,
        i * board_length:(i + 1) * board_length] += 1
    return elimination_matrix


def create_one_move(move: str,
                    UP=TranslationMatrices.UP,
                    DOWN=TranslationMatrices.DOWN,
                    FORWARD=TranslationMatrices.FORWARD,
                    BACKWARD=TranslationMatrices.BACKWARD):
    up, down, forward, backward = move_string_to_directions(move)
    print(up, down, forward, backward )
    pre_matrix = np.eye(UP.shape[0])
    post_matrix = np.eye(UP.shape[0])

    if up > down:
        for i in range(up - down):
            print("UP")
            pre_matrix = np.dot(pre_matrix, UP)
    elif down > up:
        for i in range(down - up):
            print("DOWN")
            pre_matrix = np.dot(pre_matrix, DOWN)

    if forward > backward:
        for i in range(forward - backward):
            print("FORWARD")
            post_matrix = np.dot(post_matrix, FORWARD)
    elif backward > forward:
        for i in range(backward - forward):
            print("BACKWARD")
            post_matrix = np.dot(post_matrix, BACKWARD)

    return pre_matrix, post_matrix


def move_string_to_directions(move: str):
    up = 0
    down = 0
    forward = 0
    backward = 0
    number = ""
    for character in move.lower():
        if character in NUMBERS:
            number += character
        else:
            if character == 'u':
                if number is not "":
                    up += int(number)
                    number = ""
                else:
                    up += 1
            elif character == 'd':
                if number is not "":
                    down += int(number)
                    number = ""
                else:
                    down += 1

            elif character == 'f':
                if number is not "":
                    forward += int(number)
                    number = ""
                else:
                    forward += 1

            elif character == 'b':
                if number is not "":
                    backward += int(number)
                    number = ""
                else:
                    backward += 1
    return up, down, forward, backward


def apply_moves(pre_matrices, elimination_matrix, post_matrices, boards):
    print(pre_matrices.shape)
    print(elimination_matrix.shape)
    print(post_matrices.shape)
    print(boards.shape)
    return np.dot(np.multiply(np.dot(pre_matrices, boards), elimination_matrix), post_matrices)


if __name__ == '__main__':
    LENGTH = 8
    WIDTH = 8
    MOVES = ["uu,d", "f"]
    pre_matrices, elimination_matrix, post_matrices = create_move_matrices(LENGTH, WIDTH, MOVES)
    print(display_board_matrix(pre_matrices))
    print("=================")
    print(display_board_matrix(elimination_matrix))
    print("=================")
    print(display_board_matrix(post_matrices))
    print("=================")
