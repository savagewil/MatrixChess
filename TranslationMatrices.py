import numpy as np

UP = FORWARD = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0]])

DOWN = BACKWARD = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 1, 0]])

board_test = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]])
if __name__ == '__main__':
    print(board_test)
    print("FORWARD\n", np.dot(board_test, FORWARD))
    print("\n", np.dot(UP, board_test))
    print("BACKWARD\n", np.dot(board_test, BACKWARD))
    print("DOWN\n", np.dot(DOWN, board_test))
    print("================================")

    print("VERTICAL\nDOWN\nUP\n", np.concatenate((DOWN, UP), 0))

    print("HORIZON\nDOWN\nUP\n", np.concatenate((DOWN, UP), 1))

