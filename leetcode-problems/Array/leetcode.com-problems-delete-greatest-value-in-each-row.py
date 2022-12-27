

from typing import List
import time

class Solution:
    def __init__(self) -> None:
        array = []
        self.array = array
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        temp=[]
        for i in grid:
            if i == []:
                print(self.array)
                return sum(self.array)
            temp.append(max(i))
            i.remove(max(i))
        self.array.append(max(temp))
        return self.deleteGreatestValue(grid)


# solution from leetcode
# class Solution:
#     def deleteGreatestValue(self, grid: List[List[int]]) -> int:
#         for i in range(0, len(grid)):
#             grid[i].sort()
#         n = len(grid[0])
#         res = 0
#         for j in range(0, n):
#             ans = 0
#             for i in range(0, len(grid)):
#                 ans = max(ans, grid[i].pop())
#             res += ans
            
#         return res

start = time.time()
s = Solution()
# grid=[[1,2,4],[3,3,1]]
grid = [[10]]
print(s.deleteGreatestValue(grid))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
