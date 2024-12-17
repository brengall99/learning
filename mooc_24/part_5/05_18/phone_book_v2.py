phone_book = {}

while True:

    command = int(input("command (1 search, 2 add, 3 quit): "))

    if command == 1:
        search = str(input("name: "))

        if search in phone_book:
            for item in phone_book[search]:
                print(item)

        else:
            print("no number")

    elif command == 2:
        add = str(input("name: "))

        if add not in phone_book:
            to_add = input("number: ")
            phone_book[add] = [to_add]
            print("ok!")

        elif add in phone_book:
            to_add = input("number: ")
            phone_book[add].append(to_add)
            print("ok!")

    else:
        print("quitting...")
        break
