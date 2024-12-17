# Write your solution here
def longest_series_of_neighbours(numbers):
    if not numbers:
        return 0  # Handle empty list

    max_length = 1  # At least one number is a series
    current_length = 1  # Start counting the current series

    for i in range(1, len(numbers)):
        # Check if the current number and the previous one are neighbours
        if abs(numbers[i] - numbers[i - 1]) == 1:
            current_length += 1
        else:
            # Reset the current series length
            max_length = max(max_length, current_length)
            current_length = 1

    # Account for the last series being the longest
    max_length = max(max_length, current_length)

    return max_length

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))



