from typing import List


class Solution:
    #     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    #         value = sorted(list(zip(heights,names)))
    #         array = []
    #         for i in range(len(value)):
    #             array.insert(0,value[i][1])
    #         return array

    # leetcode solution
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [row[1] for row in sorted(zip(heights, names), reverse=True)]


s = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(s.sortPeople(names, heights))
