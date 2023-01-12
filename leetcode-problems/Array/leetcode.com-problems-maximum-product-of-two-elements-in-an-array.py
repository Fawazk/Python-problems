from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(nums)
        nums.sort(reverse=True)
        print(nums)
        return (nums[0] - 1) * (nums[1] - 1)


s = Solution()
nums = [3, 4, 5, 2]
print(s.maxProduct(nums))
