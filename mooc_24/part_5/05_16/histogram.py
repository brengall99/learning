# Write your solution here
def histogram(string: str) -> None:

    word_list = list(string)
    stats = {}

    for i in word_list:
        if i not in stats:
            stats[i] = "*"

        elif i in stats:
            stats[i] += "*"
        # stats[i].append("*")
    
    for key, value in stats.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    histogram("abba")