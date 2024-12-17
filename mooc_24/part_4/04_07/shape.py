# Copy here code of line function from previous exercise and use it in your solution

def line(num: int, character: str) -> None: 
    if character == "":
        character = "*"
    elif len(character) > 1:
        character = character[0:1]
    print(num*character)

def triangle(size, character):
    # You should call function line here with proper parameters
    for i in range(size + 1):
        line(i, character)

def square(size, length, character):
    # You should call function line here with proper parameters
    for i in range(length):
        line(size, character)

def shape(num1: int, char1: str, num2: int, char2: str) -> None:
    triangle(num1, char1)
    square(num1, num2, char2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")