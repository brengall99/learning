# Write your solution here
def range_of_list(list1: list) -> int:
    sorted_list = sorted(list1)
    range_list = sorted_list[-1] - sorted_list[0]
    return range_list

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = range_of_list(my_list)
    print(result)