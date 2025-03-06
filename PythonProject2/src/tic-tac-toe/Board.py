def move_to_row_col(move):
    move -= 1
    row = move // 3
    col = move % 3
    return row, col


class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, column, symbol):
        if self.board[row][column] == " ":
            self.board[row][column] = symbol
            return True
        else:
            print("Invalid move")
            return False


    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] and self.board[0][column] != " ":
                return self.board[0][column]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True
