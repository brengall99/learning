# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    # Ensure x and y are within bounds of the board
    if 0 <= x < len(game_board[0]) and 0 <= y < len(game_board):
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False  # Square already occupied
    else:
        return False  # Invalid square (out of bounds)

if __name__ == "__main__":

    game_board = [['O', '', ''], ['X', '', ''], ['', 'O', 'X']]

    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)