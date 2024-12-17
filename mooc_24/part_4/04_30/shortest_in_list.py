# Write your solution here
def shortest(list1: list) -> str:
    shortest_str = list1[0]

    for i in list1:
        if len(i) < len(shortest_str):
            shortest_str = i
        else:
            continue
    return shortest_str


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)