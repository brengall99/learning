# Write your solution here
def length_of_longest(list1: list) -> int:
    longest = ""

    for i in list1:
        if len(i) > len(longest):
            longest = i
        else:
            continue
    return len(longest)


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)