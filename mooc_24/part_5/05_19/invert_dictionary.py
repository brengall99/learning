# Write your solution here
def invert(d: dict) -> None:
    temp_dict = {value: key for key, value in d.items()}
    d.clear()  # Clear the original dictionary
    d.update(temp_dict)  # Update it with the new items

if __name__ == "__main__":

    s = {
        1: "first",
        2: "second", 
        3: "third", 
        4: "fourth"}

    invert(s)
    print(s)
