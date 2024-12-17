# Write your solution here
def sum_of_positives(list1: list) -> int:
    sum = 0
    for i in list1:
        if i > 0:
            sum += i
    return sum

if __name__ == "__main__":
    my_list = [1, -1, 2, -2, 3, -3]
    result = sum_of_positives(my_list)
    print("The result is", result)