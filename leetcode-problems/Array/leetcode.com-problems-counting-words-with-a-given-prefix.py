from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # count = 0
        # lenpref = len(pref)
        # for word in words:
        #     if word[:lenpref] == pref:
        #         count +=1
        # return count
        return sum([word.startswith(pref) for word in words])


s = Solution()
words = ["pay", "attention", "practice", "attend"]
pref = "at"
print(s.prefixCount(words, pref))
