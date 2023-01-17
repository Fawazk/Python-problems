from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            i = str(i)
            if len(i) % 2 ==0:
                count += 1
        return count
        
s = Solution()
print(s.findNumbers(nums = [12,345,2,6,7896]))