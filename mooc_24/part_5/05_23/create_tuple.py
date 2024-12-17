def create_tuple(x: int, y: int, z: int) -> tuple:
    test_list = [x, y, z]
    sorted_list = sorted(test_list)  # Get a new sorted list
    return (sorted_list[0], sorted_list[1], sorted_list[2])  # Return minimum, middle, and maximum

if __name__ == "__main__":
    print(create_tuple(1, 4, 2))  # Expected output: (1, 2, 3)