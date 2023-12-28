from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for data in words:
            if data[::-1] == data:
                return data
        return ""


s = Solution()
words = ["abc", "car", "ada", "racecar", "cool"]
print(s.firstPalindrome(words))
