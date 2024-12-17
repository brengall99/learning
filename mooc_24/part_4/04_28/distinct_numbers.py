# Write your solution here
def distinct_numbers(list1: list) -> list:
    list1.sort()
    list2 = []

    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]