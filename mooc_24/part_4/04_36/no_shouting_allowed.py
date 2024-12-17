# Write your solution here
def no_shouting(list1: list)-> list:
    list2 = []

    for i in list1:
        if i.isupper() == False:
            list2.append(i)
    return list2

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)