
from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        zippedvalue = list(zip(startTime,endTime))
        count = 0
        for i in zippedvalue:
            if i[1] >= queryTime and i[0] <= queryTime:
                count += 1
        return count

s = Solution()
print(s.busyStudent(startTime=[1,2,3],endTime=[3,2,7],queryTime=4))