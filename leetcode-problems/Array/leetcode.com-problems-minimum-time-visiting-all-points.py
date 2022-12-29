from typing import List

class Solution:    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        temp = 0
        count = 0
        for i in range(length-1):
            temp = max(abs(points[i][0] - points[i+1][0]),abs(points[i][1] - points[i+1][1]))
            count += temp
        return count

s = Solution()
points = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(points))