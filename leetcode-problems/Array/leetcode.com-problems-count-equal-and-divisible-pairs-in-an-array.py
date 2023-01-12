from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and ((i * j) % k == 0):
                    count += 1
        return count


s = Solution()
nums = [5, 5, 9, 2, 5, 5, 9, 2, 2, 5, 5, 6, 2, 2, 5, 2, 5, 4, 3]
k = 7
print(s.countPairs(nums, k))
