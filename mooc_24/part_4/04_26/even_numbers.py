def even_numbers(list1: list) -> list:

    for i in list1:
        if i % 2 == 0:
            list2.append(i)
        else:
            continue
    return list2

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)