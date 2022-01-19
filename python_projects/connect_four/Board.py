class Board:
    def __init__(self, number_of_rows=6, number_of_columns=7):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.board_state = self.initialise_board_state()

    def initialise_board_state(self):
        # 1d_nun_array = [None] * 7
        return [[None] * self.number_of_columns] * self.number_of_rows
