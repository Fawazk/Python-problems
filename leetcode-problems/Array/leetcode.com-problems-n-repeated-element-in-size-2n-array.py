from typing import List
import collections


class Solution:
    # def repeatedNTimes(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             return nums[i]
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        for num, count in nums.items():
            if count > 1:
                return num


s = Solution()
print(s.repeatedNTimes(nums=[1, 2, 3, 3]))
