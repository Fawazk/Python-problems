from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        j = 1
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[i] >= prices[j]:
        #             prices[i] = prices[i]-prices[j]
        #             break
        # return prices

        while i < len(prices) - 1 and j < len(prices):
            if prices[i] >= prices[j]:
                prices[i] = prices[i] - prices[j]
                i += 1
                j = i + 1
            elif j == len(prices) - 1:
                i += 1
                j = i + 1
            else:
                j += 1
        return prices


s = Solution()
print(s.finalPrices([8, 4, 6, 2, 3]))
