def block_correct(sudoku: list, row_start: int, col_start: int) -> bool:
    # Initialize a list to track seen numbers
    seen_numbers = []

    # Loop through the 3x3 block
    for i in range(row_start, row_start + 3):  # Rows in the block
        for j in range(col_start, col_start + 3):  # Columns in the block
            num = sudoku[i][j]
            if num == 0:  # Skip empty cells
                continue
            if num in seen_numbers:  # If number already exists, block is invalid
                return False
            seen_numbers.append(num)  # Add number to the list of seen numbers

    return True  # If no duplicates, block is valid



if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))

