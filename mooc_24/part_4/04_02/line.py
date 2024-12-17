# Write your solution here
def line(num: int, character: str) -> None: 
    if character == "":
        character = "*"
    elif len(character) > 1:
        character = character[0:1]
    print(num*character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "xab")