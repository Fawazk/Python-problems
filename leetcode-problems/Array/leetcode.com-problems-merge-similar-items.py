from typing import List


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        dic = dict(items1)
        for val in items2:
            if val[0] in dic:
                dic[val[0]] += val[1]
            else:
                dic[val[0]] = val[1]
        return sorted([[i, dic[i]] for i in dic])


s = Solution()
print(s.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
