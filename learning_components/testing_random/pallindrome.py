
def palindrome(word: str) -> bool:
    return word == word[::-1]
    
print(palindrome("cac"))
print(palindrome("caprepefds"))
