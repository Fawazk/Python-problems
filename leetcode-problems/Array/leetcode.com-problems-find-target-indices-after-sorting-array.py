from typing import List

# class Solution:
#     def targetIndices(self, nums: List[int], target: int) -> List[int]:
#         newlist = []
#         nums = sorted(nums)
#         if target in nums:
#             for i in range(len(nums)):
#                 if nums[i] == target:
#                     newlist.append(i)
#             return newlist
#         else:
#             return


class Solution:
    def targetIndices(self, N: List[int], T: int) -> List[int]:
        c = i = 0
        for n in N:
            if n < T:
                i += 1
            elif n == T:
                c += 1
        return range(i, i + c)


s = Solution()
nums = [1, 2, 5, 2, 3]
target = 5
print(s.targetIndices(nums, target))
