from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = f = 0
        perm = [0]
        for i in range(len(s)):
            if s[i] == "I":
                l += 1
                perm.append(l)
            elif s[i] == "D":
                f -=1
                perm.append(f)
        return [i - f for i in perm]

s = Solution()
print(s.diStringMatch(s="DDI"))