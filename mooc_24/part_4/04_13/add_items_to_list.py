# Write your solution here

num = int(input("How many items: "))
list1 = []

for i in range(1, num + 1):
    item = int(input(f"Item {i}: "))
    list1.append(item)

print(list1)