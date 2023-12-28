from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = []
        if n % 2 != 0:
            array.append(0)
        for i in range(1, int(n / 2) + 1):
            array.append(i)
            array.append(-i)
        return array


s = Solution()
print(s.sumZero(n=4))
