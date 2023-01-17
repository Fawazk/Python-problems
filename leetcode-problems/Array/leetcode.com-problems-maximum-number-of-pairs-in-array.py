
from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        i = 0
        count = 0
        while i<len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                count +=1
                nums.pop(i)
                nums.pop(i)
            else:
                i += 1
        return [count,len(nums)]


s = Solution()
nums = [1,3,2,1,3,2,2]
print(s.numberOfPairs(nums))