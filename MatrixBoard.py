class MatrixBoard:
    def __init__(self, board_length, board_width, total_pieces, move_rules):
        self.move_rules = move_rules
        self.board_width = board_width
        self.board_length = board_length
        self.total_pieces = total_pieces 
        self.board