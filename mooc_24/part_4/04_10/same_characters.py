def same_chars(word: str, num1: int, num2: int) -> bool:
    # Check if indices are out of bounds
    if num1 >= len(word) or num2 >= len(word):
        return False
    # Check if characters at indices are the same
    return word[num1] == word[num2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 6, 12))  # False
    print(same_chars("abc", 0, 3))          # False
    print(same_chars("hello", 0, 4))        # True
    print(same_chars("world", 1, 3))        # False