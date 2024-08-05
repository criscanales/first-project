# tic_tac_toe.py

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    win_conditions = [
        # Horizontal wins
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical wins
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal wins
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
