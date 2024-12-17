def factorials(n: int) -> int:
    # Calculate the factorial
    factorial = 1
    dicto = {}
    dicto[1] = 1

    for i in range(2, n + 1):
        factorial *= i
        dicto[i] = factorial
        print(dicto)

    return dicto 

if __name__ == "__main__": 
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])