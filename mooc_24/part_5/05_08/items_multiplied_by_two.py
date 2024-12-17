# Write your solution here
def double_items(list1: list) -> list:
    new_list = []
    for i in list1:
        new_list.append(i*2)
    
    return new_list


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)