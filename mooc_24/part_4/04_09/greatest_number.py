# Write your solution here

def greatest_number(num1: int, num2: int, num3: int) -> int:
    num4 = max(num1, num2, num3)
    return num4

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)