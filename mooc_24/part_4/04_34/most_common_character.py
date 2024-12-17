def most_common_character(string: str) -> str:
    # Dictionary to store counts and first occurrence index of each character
    counts = {}
    
    for index, char in enumerate(string):
        if char not in counts:
            counts[char] = [1, index]  # Initialize count and index of first occurrence
        else:
            counts[char][0] += 1  # Increment count for the character

    # Find the character with the maximum count, using the first occurrence as a tiebreaker
    most_common = max(counts.items(), key=lambda x: (x[1][0], -x[1][1]))[0]
    
    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))



