# write your solution here

def read_fruits() -> dict:

    fruits = {}

    with open("fruits.csv") as new_file:
        for line in new_file:
            key, value = line.strip().split(';')  
            fruits[key] = float(value)

    return fruits
            
if __name__ == "__main__":
    read_fruit()