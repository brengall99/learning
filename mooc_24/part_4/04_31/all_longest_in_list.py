# Write your solution here
def all_the_longest(list1: list) -> list:
    longest = ""
    list2 = []

    for i in list1:
        if len(i) > len(longest):
            longest = i
        max_num = len(longest)
        
    for j in list1:
        if len(j) == max_num:
            list2.append(j)

    return list2

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']