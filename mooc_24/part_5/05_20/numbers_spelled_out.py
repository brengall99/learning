def dict_of_numbers():
    # Define mappings for basic numbers
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Initialize the dictionary
    numbers = {}
    
    # Add numbers 0-9
    for i in range(10):
        numbers[i] = units[i]
    
    # Add numbers 10-19
    numbers[10] = "ten"
    for i in range(1, 10):
        numbers[10 + i] = teens[i - 1]
    
    # Add numbers 20-99
    for i in range(2, 10):
        for j in range(10):
            if j == 0:
                numbers[i * 10] = tens[i]  # "Twenty", "Thirty", etc.
            else:
                numbers[i * 10 + j] = f"{tens[i]}-{units[j]}"  # "Twenty-one", "Thirty-two", etc.
    
    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()
    # print(numbers[2])
    # print(numbers[11])
    # print(numbers[45])
    # print(numbers[99])
    # print(numbers[0])