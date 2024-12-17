# Write your solution here

index = 1
items = []
play = 'y'

while play != 'x': 
    print("The list is now",items)
    play = str(input("a(d)d, (r)emove or e(x)it: "))
    if play == 'd':
        items.append(len(items) + 1)
    elif play == 'r':
        items.pop(-1)
    elif play == 'x':
        print("Bye!")
    
