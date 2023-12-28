from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        m = {}
        count = 0
        for x in nums:
            if x + k in m:
                count += m[x + k]
            if x - k in m:
                count += m[x - k]
            if x in m:
                m[x] = m[x] + 1
            else:
                m[x] = 1
        return count


s = Solution()

nums = [1, 2, 2, 1]
k = 1
print(s.countKDifference(nums, k))
