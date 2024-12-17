# Write your solution here
def no_vowels(string: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    string2 = ""


    for i in string:
        if i not in vowels:
            string2 += i

    return string2

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))