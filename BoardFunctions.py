import numpy as np


def display_board(board):
    string = ""
    for j in range(len(board)):
        if j != 0 and j % 8 == 0:
            string += "\n"
        for i in range(len(board[j])):
            if i != 0 and i % 8 == 0:
                string += " "
            string += "%d" % board[j, i]

        string += "\n"
    return string


def create_board(board_length, board_width, piece_locations):
    board = None
    for piece_location in piece_locations:
        if board is None:
            board = generate_single_board(board_length, board_width, piece_location)
        else:
            new_board = generate_single_board(board_length, board_width, piece_location)
            board = np.concatenate((board, new_board), 1)
    return board


def generate_single_board(board_length, board_width, piece_location):
    board = np.zeros((board_length, board_width))
    board[piece_location[1], piece_location[0]] = 1
    return board
