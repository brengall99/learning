# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    test_list = []
    row = sudoku[row_no]

    # Check each number in the row
    for num in row:
        if num == 0:  # Skip empty cells (denoted by 0)
            continue
        if num in test_list:  # If number is already seen, the row is invalid
            return False
        test_list.append(num)  # Add the number to the seen list

    return True  # If no duplicates are found, the row is valid

def column_correct(sudoku: list, column_no: int) -> bool:
    column_test = []
    for row in sudoku:
        if row[column_no] == 0:
            continue
        elif row[column_no] in column_test:
            return False
        else:
            column_test.append(row[column_no])
    
    return True

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

def sudoku_grid_correct(sudoku: list) -> bool:
    # Check all rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    # Check all columns
    for col_no in range(9):
        if not column_correct(sudoku, col_no):
            return False

    # Check all 3x3 blocks
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            if not block_correct(sudoku, row_start, col_start):
                return False

    # If all checks pass, the grid is correct
    return True


if __name__ == "__main__":
    sudoku1 = [
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

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(sudoku_grid_correct(sudoku1))
    print(sudoku_grid_correct(sudoku2))