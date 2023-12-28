from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]
        

s = Solution()
words = ["leet","code"]
x = "e"
print(s.findWordsContaining(words,x))