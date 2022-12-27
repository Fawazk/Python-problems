from typing import List
import time

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        def listToString(s):
            # initialize an empty string
            str1 = ""
        
            # traverse in the string
            for ele in s:
                str1 += ele
        
            # return string
            return str1

        word1Str = listToString(word1)
        word2Str = listToString(word2)
        if word1Str == word2Str:
            return True
        else:
            return False


# Leetcode Solution
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         return True if ''.join(word1) == ''.join(word2) else False

start = time.time()
s = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]

# word1 = ["a", "cb"]
# word2 = ["ab", "c"]
# word1=["abc", "d", "defg"]
# word2 = ["abcddefg"]
returnval = s.arrayStringsAreEqual(word1,word2)
print(returnval)
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")