class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def draw(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def check_winner(self, player_symbol):
        for row in self.board:
            if all(cell == player_symbol for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player_symbol for row in range(3)):
                return True

        if all(self.board[i][i] == player_symbol for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player_symbol for i in range(3)):
            return True

        return False

    def make_move(self, position, player_symbol):
        if position < 1 or position > 9:
            return False

        position -= 1
        row = position // 3
        col = position % 3

        if self.board[row][col] == ' ':
            self.board[row][col] = player_symbol
            return True
        else:
            return False