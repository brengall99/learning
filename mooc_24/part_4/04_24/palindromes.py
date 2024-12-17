# Write your solution here

def palindromes(string1: str) -> bool:
    if len(string1) <= 1:
        return True
    if string1[0] != string1[-1]:
        return False
    return palindromes(string1[1:-1])

# Loop to keep asking for input until a valid palindrome is entered
while True:
    test_string = input("Please type in a palindrome: ")
    if palindromes(test_string):
        print(f"{test_string} is a palindrome!")
        break  # Exit the loop
    else:
        print("that wasn't a palindrome")


