# Extra little program to check words individually
import pandas as pd

class Solution:
    def isInList(self, word: str) -> bool:
        df = pd.read_csv("wordlist.txt", header=None)

        if word in df[0].values:
            return True
        else:
            return False

result = Solution().isInList("cantrnten")
print(result)