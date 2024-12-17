# Write your solution here

def spruce(num: int) -> None:
    n = 1  # Initial width
    branch = "*"  # Example branch content
    print("a spruce!")

    for i in range(num): 
        print(f"{branch:^{2 * num - 1}}")
        branch += "**"
        # print(n, branch)

    print(f"{"*":^{2 * num - 1}}")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)