from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)
        for i in range(length):
            total += mat[i][i]
            total += mat[i][(length - 1) - i]
        if length % 2 != 0:
            total -= mat[int(length / 2)][int(length / 2)]
        return total


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.diagonalSum(mat))
