from typing import List

# using for loop enumerate
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            if num % 2 == 0:
                nums.pop(i)
                nums.insert(0,num)
        return nums


# # using for loop range
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         temp=0
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 temp = nums[i]
#                 nums.pop(i)
#                 nums.insert(0,temp)
#         return nums


s = Solution()
print(s.sortArrayByParity([3,1,2,4]))