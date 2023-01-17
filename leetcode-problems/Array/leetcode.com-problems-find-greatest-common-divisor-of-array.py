from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        minvalue = nums[0]
        maxvalue = nums[len(nums)-1]
        i = 1
        while i<= minvalue:
            if minvalue%i == 0 and maxvalue%i == 0:
                temp = i
            i +=1
        return temp

# Leetcode solution
# class Solution:
#     def fastGcd(self, n1, n2):
#         bigger = max(n1, n2)
#         smaller = min(n1, n2)

#         if smaller == 0:
#             return bigger
#         return self.fastGcd((bigger - smaller), smaller)
#     def findGCD(self, nums: List[int]) -> int:
#         return self.fastGcd(max(nums), min(nums))

s = Solution()
print(s.findGCD(nums=[2,5,6,9,10]))
