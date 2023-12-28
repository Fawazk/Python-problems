from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        v1 = nums[0]
        v2 = nums[1]
        v3 = nums[l - 1]
        v4 = nums[l - 2]
        return abs((v1 * v2) - (v3 * v4))


s = Solution()
nums = [5, 6, 2, 7, 4]
print(s.maxProductDifference(nums))
