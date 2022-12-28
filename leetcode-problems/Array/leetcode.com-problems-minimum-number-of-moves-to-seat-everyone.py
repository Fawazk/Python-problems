from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        count = 0
        students = sorted(students)
        for i in range(len(seats)):
            count += abs(seats[i] - students[i])
        return count


s = Solution()
seats = [2, 2, 6, 6]
students = [1, 3, 2, 6]
print(s.minMovesToSeat(seats, students))
