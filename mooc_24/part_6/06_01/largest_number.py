# write your solution here
def largest() -> int:
    largest_num = float('-inf')

    with open("numbers.txt", "r") as file:
        for line in file: 
            num = int(line.strip())
            if num > largest_num:
                largest_num = num

    return largest_num

if __name__ == "__main__":
    largest = largest()
    print(largest)

    