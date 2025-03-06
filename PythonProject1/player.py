class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                position = int(input(f"Player {self.symbol}, enter position (1-9): "))
                if 1 <= position <= 9:
                    if board.make_move(position, self.symbol):
                        return
                    else:
                        print("That cell is already taken. Try again.")
                else:
                    print("Invalid input. Position must be between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")