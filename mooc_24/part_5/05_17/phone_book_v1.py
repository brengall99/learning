# Write your solution here
phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        search = str(input("name: "))
        if search in phone_book:
            print(phone_book[search])
        else:
            print("no number")

    elif command == 2:
        add = str(input("name: "))
        if add in phone_book:
            phone_book[add] = input("number: ")
            print("ok!")
        else:
            phone_book[add] = input("number: ")
            print("ok!")
    else:
        print("quitting...")
        break