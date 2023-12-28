from typing import List


# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         count = 0
#         totalcount = 0
#         for j in words:
#             for k in j:
#                 if k not in allowed:
#                     break
#                 else:
#                     count += 1
#             if len(j) == count:
#                 totalcount += 1
#             count = 0

#         return totalcount


# leetcode solution
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        return len(words) - count


s = Solution()
allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
print(s.countConsistentStrings(allowed, words))
