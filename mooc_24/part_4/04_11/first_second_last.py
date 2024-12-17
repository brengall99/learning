def first_word(sentence: str) -> str:
    # Find the first space to extract the first word
    if " " in sentence:
        return sentence[:sentence.find(" ")]
    return sentence  # If no space, the entire sentence is the first word

def second_word(sentence: str) -> str:
    # Find the first space and extract the remainder of the sentence
    first_space = sentence.find(" ")
    if first_space == -1:
        return ""  # No second word if no space
    remainder = sentence[first_space + 1:]
    # Find the next space to get the second word
    second_space = remainder.find(" ")
    if second_space == -1:
        return remainder  # Remainder is the second word if no more spaces
    return remainder[:second_space]

def last_word(sentence: str) -> str:
    # Find the last space and extract the last word
    last_space = sentence.rfind(" ")
    if last_space == -1:
        return sentence  # If no space, the entire sentence is the last word
    return sentence[last_space + 1:]

# You can test your functions with the following block
if __name__ == "__main__":
    print(first_word("Hello world!"))      # Output: "Hello"
    print(second_word("Hello world!"))     # Output: "world!"
    print(last_word("Hello world!"))       # Output: "world!"
    print(first_word("SingleWord"))        # Output: "SingleWord"
    print(second_word("SingleWord"))       # Output: ""
    print(last_word("SingleWord"))         # Output: "SingleWord"