# Write your solution here
def everything_reversed(list1: list) -> list:
    reversed_list = []
    for i in list1:
        reversed_list.append(i[::-1])

    return reversed_list[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]

    # my_list = ['abc']

    new_list = everything_reversed(my_list)
    print(new_list)