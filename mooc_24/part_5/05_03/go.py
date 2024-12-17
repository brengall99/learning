# Write your solution here
def who_won(game_board: list) -> int:
    count1, count2 = 0, 0

    for i in game_board:
        for j in i:
            if j == 1:
                count1 += 1
            elif j == 2:
                count2 += 1
        
    if count1 < count2:
        return 2
    if count1 > count2:
        return 1
    elif count1 == count2:
        return 0

if __name__ == "__main__":
    test_board = [
        [0, 1, 2],
        [0, 0, 1],
        [1, 1, 0]
    ]

    print(who_won(test_board))