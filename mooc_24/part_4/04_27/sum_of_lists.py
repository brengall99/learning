# Write your solution here
def list_sum(list1: list, list2: list) -> list:
    list3 = []
    for i in range(len(list1)): 
        list3.append(list1[i] + list2[i])
    return list3

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]