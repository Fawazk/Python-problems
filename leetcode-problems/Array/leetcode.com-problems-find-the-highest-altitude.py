from typing import List
import itertools


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        for i in range(len(gain) - 1):
            gain.insert(i + 1, gain[i] + gain[i + 1])
            gain.pop(i + 2)
        return max(gain)

        # leetcode solution
        # return max(list(itertools.accumulate(gain))+[0])


# [0,-4,-7,-9,-10,-6,-3,-1]

s = Solution()
gain = [-5, 1, 5, 0, -7]
print(s.largestAltitude(gain))
