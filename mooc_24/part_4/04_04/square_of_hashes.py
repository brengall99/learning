# Write your solution here

def line(num: int, character: str) -> None: 
    if character == "":
        character = "*"
    elif len(character) > 1:
        character = character[0:1]
    print(num*character)

def square_of_hashes(height):
    # You should call function line here with proper parameters
    for i in range(height):
        line(height, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(2)

