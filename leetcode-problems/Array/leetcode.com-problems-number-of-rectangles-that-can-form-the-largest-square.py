
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = {}
        for i in range(len(rectangles)):
            if rectangles[i][0] < rectangles[i][1]:
                if rectangles[i][0] in temp:
                    temp[rectangles[i][0]] += 1
                else:
                    temp[rectangles[i][0]] = 1
            else:
                if rectangles[i][1] in temp:
                    temp[rectangles[i][1]] += 1
                else:
                    temp[rectangles[i][1]] = 1
        maxvalue = max(temp)
        return temp[maxvalue]

        # Leetcode Solution

        # squares=[min(i) for i in rectangles]
        # return squares.count(max(squares))

s = Solution()
rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(s.countGoodRectangles(rectangles))