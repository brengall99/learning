# Write your solution here
def longest(strings: list) -> str:
    len_longest = 0
    
    for i in range(0, len(strings)):
        if len(strings[i]) > len_longest:
            longest = strings[i]
            len_longest = len(strings[i])
    
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))