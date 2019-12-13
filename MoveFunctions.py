import numpy as np
import TranslationMatrices
from BoardFunctions import display_board

NUMBERS = "1234567890"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def create_move_matrices(move_array):
    pre_matrix = None
    post_matrix = None
    elimination_matrix = None
    return pre_matrix, elimination_matrix, post_matrix


def create_elimination_matrix(board_length, board_width, move_count_array):
    length = board_length * sum(move_count_array)
    width = board_width * len(move_count_array)
    elimination_matrix = np.zeros((length, width))
    y_displacement = 0
    for piece_index in range(len(move_count_array)):
        for move_index in range(move_count_array[piece_index]):
            elimination_matrix[y_displacement * board_width:(y_displacement + 1) * board_width, piece_index * board_length:(piece_index + 1) * board_length] += 1
            y_displacement += 1
    return elimination_matrix

def create_one_move(move: str,
                    UP=TranslationMatrices.UP,
                    DOWN=TranslationMatrices.DOWN,
                    FORWARD=TranslationMatrices.FORWARD,
                    BACKWARD=TranslationMatrices.BACKWARD):
    up, down, forward, backward = move_string_to_directions

    pre_matrix = None
    post_matrix = None

    if up > down:
        for i in range(up - down):
            if pre_matrix is None:
                pre_matrix = UP
            else:
                pre_matrix = np.dot(pre_matrix, UP)
    elif down > up:
        for i in range(down - up):
            if pre_matrix is None:
                pre_matrix = DOWN
            else:
                pre_matrix = np.dot(pre_matrix, DOWN)

    if forward > backward:
        for i in range(forward - backward):
            if post_matrix is None:
                post_matrix = FORWARD
            else:
                post_matrix = np.dot(post_matrix, FORWARD)
    elif backward < forward:
        for i in range(backward - forward):
            if post_matrix is None:
                post_matrix = BACKWARD
            else:
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

if __name__ == '__main__':
    elimination_matrix = create_elimination_matrix(8,8,[2,1,1,1])
    print(display_board(elimination_matrix))
