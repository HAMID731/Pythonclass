from Board import Board
from player import Player

def play_tic_tac_toe():
    board = Board()
    player_x = Player('X')
    player_o = Player('O')
    current_player = player_x

    while True:
        print("""🥷Welcome to Squid Game🥷
        Round
        """)
        board.draw()
        current_player.get_move(board)

        if board.check_winner(current_player.symbol):
            board.draw()
            print(f"Player {current_player.symbol} wins!")
            break

        if board.is_full():
            board.draw()
            print("It's a tie!")
            break

        current_player = player_o if current_player == player_x else player_x

if __name__ == "__main__":
    play_tic_tac_toe()