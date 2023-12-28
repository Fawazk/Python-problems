from typing import List
import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        temp = []
        for i in range(len(nums) - 1):
            if nums[i] in nums[i + 1 : len(nums)]:
                if nums[i] in temp:
                    temp.insert(0, nums[i])
                else:
                    temp.insert(0, nums[i])
                    temp.insert(0, nums[i])
        return sum(nums) - sum(temp)


# Leetcode solution
# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         coun = collections.Counter(nums)
#         outsum = 0
#         for num , count in coun.items():
#             if count == 1 :
#                 outsum = outsum +num
#         return outsum

s = Solution()
print(s.sumOfUnique(nums=[1, 2, 3, 2]))
