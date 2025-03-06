import Board
import Player

def get_player_move(player):
    while True:
        try:
            move = int(input(f"{player.symbol}, enter move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Move must be 1-9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def switch_player(current_player, player1, player2):
    if current_player == player1:
        return player2
    else:
        return player1

player1_symbol = input("Player 1, choose your symbol (e.g., X, O, @): ")
player2_symbol = input("Player 2, choose your symbol: ")
player1 = Player.Player(player1_symbol)
player2 = Player.Player(player2_symbol)
board = Board
current_player = player1
board.display_board()

while True:
    move = get_player_move(current_player)
    row, col = board.move_to_row_col(move)
    if board.make_move(row, col, current_player.symbol):
        board.display_board()
        winner = board.check_win()
        if winner:
            print(f"Player {winner} wins!")
            break
        elif board.is_board_full():
            print("It's a tie!")
            break
        else:
            current_player = switch_player(current_player, player1, player2)
    else:
        print("That spot is taken. Try again.")

print("Game Over")