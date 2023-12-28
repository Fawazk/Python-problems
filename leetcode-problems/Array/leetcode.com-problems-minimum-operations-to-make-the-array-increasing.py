from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i = 0
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                count += nums[i] + 1 - nums[i + 1]
                print((nums[i] + 1 - nums[i + 1]))
                nums[i + 1] = nums[i] + 1
        print(nums)
        return count


s = Solution()
nums = [1, 5, 2, 4, 1]
print(s.minOperations(nums))
