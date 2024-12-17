# Copy here code of line function from previous exercise
def line(num: int, character: str) -> None: 
    if character == "":
        character = "*"
    elif len(character) > 1:
        character = character[0:1]
    print(num*character)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size + 1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
