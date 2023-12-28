from typing import List


# leetcode solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums[::2])
        return sum(nums[::2])


s = Solution()
print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
