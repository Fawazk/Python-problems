from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        returnarray = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if k < len(arr) and (abs(arr[i]-arr[j]) <= a) and (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                        returnarray.append((arr[i],arr[j],arr[k]))
        return len(returnarray)

        
s = Solution()
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

print(s.countGoodTriplets(arr,a,b,c))


# 0 <= i < j < k < arr.length
# |arr[i]-arr[j] <= a
# |arr[j]-arr[k] <= b
# |arr[i]-arr[k] <= c