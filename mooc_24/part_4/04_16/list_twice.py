# Write your solution here
unordered_list = []

while True: 
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    else: 
        unordered_list.append(item)
        print("The list now:",unordered_list)
        print("The list in order:",sorted(unordered_list))
